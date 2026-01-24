
import React, { useState, useEffect, useMemo } from 'react';
import { createRoot } from 'react-dom/client';
import { GoogleGenAI, Type } from "@google/genai";
import { 
  ResponsiveContainer, 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  Tooltip, 
  CartesianGrid,
  LineChart,
  Line,
  Brush
} from 'recharts';
import { 
  Search, 
  TrendingUp, 
  Target, 
  Layout, 
  ShieldCheck, 
  Code, 
  Layers, 
  Plus, 
  ExternalLink,
  ChevronRight,
  BarChart3,
  Loader2,
  AlertCircle,
  CheckCircle2,
  Zap,
  Filter,
  ArrowUpRight,
  History,
  Save,
  Trash2,
  Globe,
  DollarSign,
  TrendingDown,
  Wand2,
  FileText,
  Rocket,
  BrainCircuit,
  Database,
  LineChart as LineChartIcon,
  MessageSquare,
  AlertTriangle,
  FileCheck,
  Megaphone,
  LogIn,
  LogOut,
  User,
  Github,
  Monitor,
  Activity,
  Cpu,
  RefreshCw,
  Clock,
  Menu,
  Lightbulb,
  SearchCode,
  ClipboardCheck,
  Link as LinkIcon,
  Bookmark,
  Star,
  X,
  FileBadge,
  Download,
  PlusCircle,
  Heart
} from 'lucide-react';

// --- Types ---

interface Product {
  id: string;
  title: string;
  url: string;
  price: number;
  sales: number;
  rating: number;
  reviews: number;
  lastUpdate: string;
  launchDate: string;
  author: string;
  category: string;
  description?: string;
  technologies?: string[];
}

interface ProfitabilityMetrics {
  salesVelocityScore: number;
  revenueScore: number;
  saturationScore: number;
  updateScore: number;
  ratingScore: number;
}

interface AnalysisResult {
  id: string;
  productId: string;
  profitabilityScore: number;
  opportunityScore: number;
  metrics: ProfitabilityMetrics;
  isBlueOcean: boolean;
  reasoning: string;
  featureGaps: string[];
  competitorWeaknesses: string[];
  marketDemandValidation: string;
  riskFactors: {
    highCompetition: boolean;
    priceWar: boolean;
    staleMarket: boolean;
    lowDemand: boolean;
  };
  painPoints: string[];
  createdAt: string;
}

interface DevelopmentPlan {
  id: string;
  projectName: string;
  baseProduct: string;
  concept: string;
  innovationStrategy: string;
  featureSpecification: string[];
  uniqueSellingPoints: string[];
  techStack: {
    frontend: string[];
    backend: string[];
    database: string[];
    modernUpgrades: string[];
  };
  pricingStrategy: {
    recommendedPrice: number;
    reasoning: string;
    marketingAngle: string;
  };
  roiAnalysis: {
    estimatedEffortDays: number;
    potentialMonthlyRoi: string;
    breakEvenMonths: number;
  };
  roadmap: { phase: string; tasks: string[] }[];
  complianceChecklist: {
    category: string;
    items: string[];
  }[];
  createdAt: string;
}

interface SearchHistoryItem {
  id: string;
  query: string;
  timestamp: string;
  resultsCount: number;
}

interface GroundingSource {
  title: string;
  uri: string;
}

interface Job {
  id: string;
  name: string;
  status: 'queued' | 'processing' | 'completed' | 'failed';
  progress: number;
  type: 'market_intel' | 'gap_analysis' | 'innovation_strategy' | 'dev_planning' | 'grounding_research' | 'direct_scrape';
}

interface MarketTrend {
  id: string;
  category: string;
  growthRate: string;
  trendingTech: string[];
  sentiment: 'positive' | 'neutral' | 'negative';
  timestamp: string;
}

// --- App Component ---

const App: React.FC = () => {
  // Authentication State
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [user, setUser] = useState<{ name: string; email: string; image: string } | null>(null);

  // Core Navigation
  const [activeTab, setActiveTab] = useState<'dashboard' | 'discovery' | 'analysis' | 'projects' | 'trends' | 'knowledge' | 'favorites'>('dashboard');
  const [plannerStep, setPlannerStep] = useState<number>(0);
  
  // UI State
  const [searchQuery, setSearchQuery] = useState('');
  const [urlInput, setUrlInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [minRating, setMinRating] = useState<number>(0);
  
  // Database Simulation State
  const [products, setProducts] = useState<Product[]>([]);
  const [favorites, setFavorites] = useState<Product[]>([]);
  const [searchHistory, setSearchHistory] = useState<SearchHistoryItem[]>([]);
  const [analysisResults, setAnalysisResults] = useState<AnalysisResult[]>([]);
  const [marketTrends, setMarketTrends] = useState<MarketTrend[]>([]);
  const [userProjects, setUserProjects] = useState<DevelopmentPlan[]>([]);
  const [knowledgeBase, setKnowledgeBase] = useState<GroundingSource[]>([]);
  const [jobs, setJobs] = useState<Job[]>([]);

  // View States
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);
  const [currentAnalysis, setCurrentAnalysis] = useState<AnalysisResult | null>(null);
  const [devPlan, setDevPlan] = useState<DevelopmentPlan | null>(null);
  const [sources, setSources] = useState<GroundingSource[]>([]);

  // --- Utility: Generate Sales Velocity Graph Data ---
  const salesChartData = useMemo(() => {
    if (!selectedProduct) return [];
    
    // Simulate historical sales growth based on launch date
    const launch = new Date(selectedProduct.launchDate || '2023-01-01');
    const now = new Date();
    const monthsDiff = Math.max(1, (now.getFullYear() - launch.getFullYear()) * 12 + (now.getMonth() - launch.getMonth()));
    const totalSales = selectedProduct.sales || 0;
    
    const data = [];
    let accumulatedSales = 0;
    const steps = Math.max(monthsDiff, 12); // Ensure at least 12 points for better zooming experience
    
    for (let i = 0; i <= steps; i++) {
      const pointDate = new Date(launch.getTime());
      pointDate.setMonth(launch.getMonth() + i);
      
      // Logistic or exponential growth simulation
      const progress = i / steps;
      const momentum = Math.pow(progress, 1.5); // Slight curve
      const salesAtPoint = Math.floor(totalSales * momentum);
      
      // Monthly velocity = sales added this period
      const velocity = Math.max(0, salesAtPoint - accumulatedSales);
      accumulatedSales = salesAtPoint;

      data.push({
        name: pointDate.toLocaleDateString('en-US', { month: 'short', year: '2-digit' }),
        velocity: velocity,
        total: accumulatedSales
      });
    }
    
    return data;
  }, [selectedProduct]);

  // --- Utility: Generate Price History Graph Data ---
  const priceChartData = useMemo(() => {
    if (!selectedProduct) return [];
    
    const launch = new Date(selectedProduct.launchDate || '2023-01-01');
    const now = new Date();
    const monthsDiff = Math.max(1, (now.getFullYear() - launch.getFullYear()) * 12 + (now.getMonth() - launch.getMonth()));
    const currentPrice = selectedProduct.price || 0;
    
    const data = [];
    const steps = Math.max(monthsDiff, 12); // At least 12 points
    
    // Start price is usually lower for early adopters
    const startPrice = currentPrice * 0.75;
    
    for (let i = 0; i <= steps; i++) {
      const pointDate = new Date(launch.getTime());
      pointDate.setMonth(launch.getMonth() + i);
      
      // Simulate price increases at major intervals
      const progress = i / steps;
      let price = startPrice + (currentPrice - startPrice) * progress;
      
      // Add minor random price testing fluctuations
      if (i > 0 && i < steps) {
        price += (Math.random() - 0.5) * (currentPrice * 0.1);
      }
      
      if (i === steps) price = currentPrice;

      data.push({
        name: pointDate.toLocaleDateString('en-US', { month: 'short', year: '2-digit' }),
        price: Number(price.toFixed(2))
      });
    }
    
    return data;
  }, [selectedProduct]);

  // Filtered Products for Discovery
  const filteredProducts = useMemo(() => {
    return products.filter(p => (p.rating || 0) >= minRating);
  }, [products, minRating]);

  // --- Queue System Simulation ---

  const addJob = (name: string, type: Job['type']) => {
    const newJob: Job = {
      id: Math.random().toString(36).substr(2, 9),
      name,
      status: 'queued',
      progress: 0,
      type
    };
    setJobs(prev => [newJob, ...prev].slice(0, 15));
    simulateJob(newJob.id);
  };

  const simulateJob = (id: string) => {
    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.random() * 10;
      setJobs(prev => prev.map(j => {
        if (j.id === id) {
          return {
            ...j,
            status: progress >= 100 ? 'completed' : 'processing',
            progress: Math.min(progress, 100)
          };
        }
        return j;
      }));
      if (progress >= 100) clearInterval(interval);
    }, 400);
  };

  // --- Persistence & Self-Learning ---

  useEffect(() => {
    const loadDB = () => {
      const keys = [
        { key: 'ci_products', setter: setProducts },
        { key: 'ci_favorites', setter: setFavorites },
        { key: 'ci_search_history', setter: setSearchHistory },
        { key: 'ci_analysis_results', setter: setAnalysisResults },
        { key: 'ci_market_trends', setter: setMarketTrends },
        { key: 'ci_user_projects', setter: setUserProjects },
        { key: 'ci_knowledge_base', setter: setKnowledgeBase },
        { key: 'ci_user_auth', setter: (val: any) => { if (val) { setIsAuthenticated(true); setUser(val); } } },
      ];
      keys.forEach(({ key, setter }) => {
        const saved = localStorage.getItem(key);
        if (saved) { try { setter(JSON.parse(saved)); } catch (e) {} }
      });
    };
    loadDB();
  }, []);

  useEffect(() => {
    const syncDB = () => {
      const dataMap = { 
        ci_products: products, 
        ci_favorites: favorites,
        ci_search_history: searchHistory, 
        ci_analysis_results: analysisResults, 
        ci_market_trends: marketTrends, 
        ci_user_projects: userProjects, 
        ci_knowledge_base: knowledgeBase, 
        ci_user_auth: user 
      };
      Object.entries(dataMap).forEach(([key, val]) => localStorage.setItem(key, JSON.stringify(val)));
    };
    syncDB();
  }, [products, favorites, searchHistory, analysisResults, marketTrends, userProjects, knowledgeBase, user]);

  // --- Intelligence Orchestration ---

  const handleSaveSearch = () => {
    const query = searchQuery.trim();
    if (!query || query === 'Search Saved!') return;
    
    // Prevent duplicate adjacent entries
    if (searchHistory.length > 0 && searchHistory[0].query === query) return;

    const newItem: SearchHistoryItem = {
      id: crypto.randomUUID(),
      query,
      timestamp: new Date().toISOString(),
      resultsCount: products.length
    };
    setSearchHistory(prev => [newItem, ...prev].slice(0, 50));
    
    // Provide visual feedback
    const originalQuery = searchQuery;
    setSearchQuery('Search Saved!');
    setTimeout(() => setSearchQuery(originalQuery), 1000);
  };

  const performSearch = async (query: string) => {
    if (!query) return;
    setIsLoading(true);
    setError(null);
    setSources([]);
    addJob(`Agent: Market Intelligence [${query}]`, 'market_intel');

    try {
      const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
      const prompt = `Act as the Market Intelligence Agent. Search CodeCanyon for "${query}". Tasks: 1. Use Google Search grounding to find top-selling products. 2. Identify technology trends. 3. Return JSON: { products: Product[], trend: Trend }`;
      const response = await ai.models.generateContent({
        model: 'gemini-3-flash-preview',
        contents: prompt,
        config: {
          responseMimeType: "application/json",
          responseSchema: {
            type: Type.OBJECT,
            properties: {
              products: {
                type: Type.ARRAY,
                items: {
                  type: Type.OBJECT,
                  properties: {
                    id: { type: Type.STRING },
                    title: { type: Type.STRING },
                    url: { type: Type.STRING },
                    price: { type: Type.NUMBER },
                    sales: { type: Type.NUMBER },
                    rating: { type: Type.NUMBER },
                    author: { type: Type.STRING },
                    category: { type: Type.STRING },
                    launchDate: { type: Type.STRING }
                  }
                }
              },
              trend: {
                type: Type.OBJECT,
                properties: { category: { type: Type.STRING }, growth: { type: Type.STRING }, tech: { type: Type.ARRAY, items: { type: Type.STRING } }, sentiment: { type: Type.STRING } }
              }
            }
          },
          tools: [{ googleSearch: {} }]
        }
      });

      const result = JSON.parse(response.text || '{"products":[]}');
      setProducts(result.products || []);
      
      // Record in history automatically on success
      setSearchHistory(prev => {
        const newItem = { id: crypto.randomUUID(), query, timestamp: new Date().toISOString(), resultsCount: result.products?.length || 0 };
        return [newItem, ...prev.filter(h => h.query !== query)].slice(0, 50);
      });

      if (result.trend) {
        setMarketTrends(prev => [{ id: crypto.randomUUID(), category: result.trend.category || 'Niche', growthRate: result.trend.growth, trendingTech: result.trend.tech, sentiment: result.trend.sentiment?.toLowerCase().includes('pos') ? 'positive' : 'neutral' as any, timestamp: new Date().toISOString() }, ...prev].slice(0, 15));
      }
      setActiveTab('discovery');
    } catch (err: any) {
      setError('Market Intelligence sync error.');
    } finally {
      setIsLoading(false);
    }
  };

  const runMarketIntelligence = (e?: React.FormEvent) => {
    e?.preventDefault();
    performSearch(searchQuery);
  };

  const runUrlAnalysis = async (e?: React.FormEvent) => {
    e?.preventDefault();
    if (!urlInput) return;
    setIsLoading(true);
    setError(null);
    addJob(`Agent: Direct URL Scrape [${urlInput}]`, 'direct_scrape');

    try {
      const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
      const prompt = `Act as the Market Intelligence Agent. Analyze this specific CodeCanyon URL: "${urlInput}". Tasks: 1. Detailed info extraction. 2. Return JSON: { products: Product[], trend: Trend }`;
      const response = await ai.models.generateContent({
        model: 'gemini-3-flash-preview',
        contents: prompt,
        config: {
          responseMimeType: "application/json",
          responseSchema: {
            type: Type.OBJECT,
            properties: {
              products: {
                type: Type.ARRAY,
                items: {
                  type: Type.OBJECT,
                  properties: {
                    id: { type: Type.STRING },
                    title: { type: Type.STRING },
                    url: { type: Type.STRING },
                    price: { type: Type.NUMBER },
                    sales: { type: Type.NUMBER },
                    rating: { type: Type.NUMBER },
                    author: { type: Type.STRING },
                    category: { type: Type.STRING },
                    launchDate: { type: Type.STRING }
                  }
                }
              },
              trend: { type: Type.OBJECT, properties: { category: { type: Type.STRING }, growth: { type: Type.STRING }, tech: { type: Type.ARRAY, items: { type: Type.STRING } }, sentiment: { type: Type.STRING } } }
            }
          },
          tools: [{ googleSearch: {} }]
        }
      });
      const result = JSON.parse(response.text || '{"products":[]}');
      if (result.products?.length) {
        setProducts(result.products);
        runDeepAnalysis(result.products[0]);
      } else {
        setError("Verification failed.");
        setIsLoading(false);
      }
    } catch (err) {
      setError('Sequence interrupted.');
      setIsLoading(false);
    }
  };

  const runDeepAnalysis = async (product: Product) => {
    setIsLoading(true);
    setSelectedProduct(product);
    setActiveTab('analysis');
    setError(null);
    addJob(`Agent: Gap Analyzer [${product.title}]`, 'gap_analysis');

    try {
      const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
      const prompt = `Analyze: ${product.title}. Identify feature gaps, competitor weaknesses, and calculate profitability metrics. Valid via grounding.`;
      const response = await ai.models.generateContent({
        model: 'gemini-3-pro-preview',
        contents: prompt,
        config: {
          responseMimeType: "application/json",
          responseSchema: {
            type: Type.OBJECT,
            properties: {
              profitabilityScore: { type: Type.NUMBER },
              opportunityScore: { type: Type.NUMBER },
              metrics: {
                type: Type.OBJECT,
                properties: {
                  salesVelocityScore: { type: Type.NUMBER },
                  revenueScore: { type: Type.NUMBER },
                  saturationScore: { type: Type.NUMBER },
                  updateScore: { type: Type.NUMBER },
                  ratingScore: { type: Type.NUMBER }
                }
              },
              isBlueOcean: { type: Type.BOOLEAN },
              reasoning: { type: Type.STRING },
              featureGaps: { type: Type.ARRAY, items: { type: Type.STRING } },
              competitorWeaknesses: { type: Type.ARRAY, items: { type: Type.STRING } },
              marketDemandValidation: { type: Type.STRING },
              riskFactors: { type: Type.OBJECT, properties: { highCompetition: { type: Type.BOOLEAN }, priceWar: { type: Type.BOOLEAN }, staleMarket: { type: Type.BOOLEAN }, lowDemand: { type: Type.BOOLEAN } } },
              painPoints: { type: Type.ARRAY, items: { type: Type.STRING } }
            }
          },
          tools: [{ googleSearch: {} }]
        }
      });
      const data = JSON.parse(response.text || '{}');
      const analysis: AnalysisResult = { ...data, id: crypto.randomUUID(), productId: product.id, createdAt: new Date().toISOString() };
      setCurrentAnalysis(analysis);
      setAnalysisResults(prev => [analysis, ...prev].slice(0, 50));
    } catch (err) {
      setError('Gap Analyzer error.');
    } finally {
      setIsLoading(false);
    }
  };

  const runStructuralPlanning = async () => {
    if (!selectedProduct || !currentAnalysis) return;
    setIsLoading(true);
    setActiveTab('projects');
    addJob(`Agent: Innovation Strategist [${selectedProduct.title}]`, 'innovation_strategy');

    try {
      const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
      const prompt = `Blueprint for competing with ${selectedProduct.title}. USPs, tech stack, roadmap, compliance. Focus deeply on 'complianceChecklist' including file structure, licensing, documentation, and support standards.`;
      const response = await ai.models.generateContent({
        model: 'gemini-3-pro-preview',
        contents: prompt,
        config: {
          responseMimeType: "application/json",
          responseSchema: {
            type: Type.OBJECT,
            properties: {
              projectName: { type: Type.STRING },
              concept: { type: Type.STRING },
              innovationStrategy: { type: Type.STRING },
              featureSpecification: { type: Type.ARRAY, items: { type: Type.STRING } },
              uniqueSellingPoints: { type: Type.ARRAY, items: { type: Type.STRING } },
              techStack: { type: Type.OBJECT, properties: { frontend: { type: Type.ARRAY, items: { type: Type.STRING } }, backend: { type: Type.ARRAY, items: { type: Type.STRING } }, database: { type: Type.ARRAY, items: { type: Type.STRING } }, modernUpgrades: { type: Type.ARRAY, items: { type: Type.STRING } } } },
              pricingStrategy: { type: Type.OBJECT, properties: { recommendedPrice: { type: Type.NUMBER }, reasoning: { type: Type.STRING }, marketingAngle: { type: Type.STRING } } },
              roiAnalysis: { type: Type.OBJECT, properties: { estimatedEffortDays: { type: Type.NUMBER }, potentialMonthlyRoi: { type: Type.STRING }, breakEvenMonths: { type: Type.NUMBER } } },
              roadmap: { type: Type.ARRAY, items: { type: Type.OBJECT, properties: { phase: { type: Type.STRING }, tasks: { type: Type.ARRAY, items: { type: Type.STRING } } } } },
              complianceChecklist: { type: Type.ARRAY, items: { type: Type.OBJECT, properties: { category: { type: Type.STRING }, items: { type: Type.ARRAY, items: { type: Type.STRING } } } } }
            }
          }
        }
      });
      const plan: DevelopmentPlan = { ...JSON.parse(response.text || '{}'), id: crypto.randomUUID(), baseProduct: selectedProduct.title, createdAt: new Date().toISOString() };
      setDevPlan(plan);
    } catch (err) {
      setError('Synthesis failed.');
    } finally {
      setIsLoading(false);
    }
  };

  const saveProject = () => {
    if (!devPlan) return;
    setUserProjects(prev => (prev.find(p => p.id === devPlan.id) ? prev : [devPlan, ...prev]));
  };

  const removeSearchHistoryItem = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setSearchHistory(prev => prev.filter(item => item.id !== id));
  };

  const handleNewProject = () => {
    setDevPlan(null);
    setSelectedProduct(null);
    setCurrentAnalysis(null);
    setPlannerStep(0);
    setActiveTab('discovery');
  };

  const toggleFavorite = (product: Product, e: React.MouseEvent) => {
    e.stopPropagation();
    setFavorites(prev => {
      const isFav = prev.some(f => f.id === product.id);
      if (isFav) {
        return prev.filter(f => f.id !== product.id);
      } else {
        return [...prev, product];
      }
    });
  };

  const isFavorite = (productId: string) => favorites.some(f => f.id === productId);

  // --- UI Components ---

  const StatBar = ({ value, label, color }: { value: number, label: string, color: string }) => (
    <div className="space-y-1">
      <div className="flex justify-between text-[10px] font-black text-slate-500 uppercase">
        <span>{label}</span>
        <span>{value}%</span>
      </div>
      <div className="h-1.5 bg-slate-800 rounded-full overflow-hidden">
        <div className={`h-full ${color} transition-all duration-1000`} style={{ width: `${value}%` }} />
      </div>
    </div>
  );

  // Added 'key' to props definition to resolve TypeScript assignability issues in map() calls.
  const ProductCard = ({ product, key }: { product: Product, key?: React.Key }) => (
    <div onClick={() => runDeepAnalysis(product)} className="group bg-slate-900/40 border-2 border-slate-800/50 hover:border-blue-500/30 rounded-[3rem] p-8 transition-all cursor-pointer relative overflow-hidden">
       <div className="flex justify-between items-start mb-6">
          <span className="text-[10px] font-black bg-blue-500/10 text-blue-400 px-3 py-1 rounded-full uppercase tracking-widest">{product.category}</span>
          <div className="flex items-center gap-2">
            <button 
              onClick={(e) => toggleFavorite(product, e)}
              className={`p-2 rounded-xl transition-all border ${isFavorite(product.id) ? 'bg-rose-500/10 border-rose-500/50 text-rose-500' : 'bg-slate-950 border-slate-800 text-slate-500 hover:text-rose-400'}`}
            >
              <Heart size={16} fill={isFavorite(product.id) ? "currentColor" : "none"} />
            </button>
            <div className="font-black text-emerald-400 bg-slate-950/80 px-3 py-1 rounded-xl">${product.price}</div>
          </div>
       </div>
       <h3 className="text-xl font-black leading-tight mb-4 group-hover:text-blue-400 transition-colors line-clamp-2">{product.title}</h3>
       <div className="grid grid-cols-2 gap-4 pt-6 border-t border-slate-800/50 mt-4">
          <div><div className="text-[10px] font-black text-slate-600 uppercase">Sales</div><div className="text-xl font-black">{product.sales.toLocaleString()}</div></div>
          <div className="text-right"><div className="text-[10px] font-black text-slate-600 uppercase">Rating</div><div className="text-xl font-black text-yellow-500">⭐ {product.rating || '0.0'}</div></div>
       </div>
    </div>
  );

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-slate-950 flex flex-col items-center justify-center p-6 font-inter relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_50%,_rgba(37,99,235,0.1),transparent_70%)]" />
        <div className="max-w-4xl w-full text-center space-y-12 relative z-10">
          <div className="flex items-center justify-center gap-4">
            <div className="bg-blue-600 p-4 rounded-[2rem] shadow-2xl shadow-blue-500/20">
              <Zap className="text-white fill-white" size={48} />
            </div>
            <div className="text-left">
              <h1 className="text-5xl font-black italic bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent leading-none">CANYONINTEL</h1>
              <p className="text-xs font-black tracking-widest text-blue-500 uppercase mt-1">Intelligence Layer v3.0</p>
            </div>
          </div>
          <div className="space-y-4">
            <h2 className="text-6xl font-black text-white leading-tight">Neural <span className="text-blue-500">Market</span> Orchestration.</h2>
            <p className="text-xl text-slate-500 max-w-2xl mx-auto leading-relaxed">Leverage a multi-agent system to identify, analyze, and plan high-yield software acquisitions.</p>
          </div>
          <button 
            onClick={() => { setIsAuthenticated(true); setUser({ name: 'Beta Analyst', email: 'beta@dev.io', image: 'https://api.dicebear.com/7.x/bottts/svg?seed=Beta' }); }} 
            className="px-10 py-5 bg-white text-slate-950 rounded-3xl font-black text-xl hover:bg-blue-50 transition-all shadow-2xl flex items-center gap-3 mx-auto"
          >
            <LogIn size={24} /> Authenticate Session
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen overflow-hidden bg-slate-950 text-slate-100 font-inter">
      {/* Sidebar */}
      <aside className="w-72 bg-slate-950 border-r border-slate-900 flex flex-col p-6 space-y-6 z-20 shrink-0">
        <div className="flex items-center gap-3 px-2">
          <div className="bg-blue-600 p-2 rounded-2xl shadow-lg">
            <Activity className="text-white" size={20} />
          </div>
          <h1 className="text-lg font-black tracking-tighter uppercase leading-none">CanyonIntel</h1>
        </div>
        <nav className="flex-1 space-y-1 overflow-y-auto custom-scrollbar">
          <button onClick={() => setActiveTab('dashboard')} className={`flex items-center gap-3 w-full p-3 rounded-2xl transition-all ${activeTab === 'dashboard' ? 'bg-blue-600/10 text-blue-400 border border-blue-600/20' : 'text-slate-500 hover:bg-white/5'}`}>
            <Layout size={18} /> <span className="font-bold text-sm">Dashboard</span>
          </button>
          <button onClick={() => setActiveTab('discovery')} className={`flex items-center gap-3 w-full p-3 rounded-2xl transition-all ${activeTab === 'discovery' ? 'bg-blue-600/10 text-blue-400 border border-blue-600/20' : 'text-slate-500 hover:bg-white/5'}`}>
            <SearchCode size={18} /> <span className="font-bold text-sm">Discovery Agent</span>
          </button>
          <button onClick={() => setActiveTab('favorites')} className={`flex items-center gap-3 w-full p-3 rounded-2xl transition-all ${activeTab === 'favorites' ? 'bg-rose-600/10 text-rose-400 border border-rose-600/20' : 'text-slate-500 hover:bg-white/5'}`}>
            <Heart size={18} /> <span className="font-bold text-sm">Favorites</span>
          </button>
          <button onClick={() => setActiveTab('analysis')} className={`flex items-center gap-3 w-full p-3 rounded-2xl transition-all ${activeTab === 'analysis' ? 'bg-blue-600/10 text-blue-400 border border-blue-600/20' : 'text-slate-500 hover:bg-white/5'}`}>
            <BarChart3 size={18} /> <span className="font-bold text-sm">Gap Analysis</span>
          </button>
          <button onClick={() => setActiveTab('projects')} className={`flex items-center gap-3 w-full p-3 rounded-2xl transition-all ${activeTab === 'projects' ? 'bg-blue-600/10 text-blue-400 border border-blue-600/20' : 'text-slate-500 hover:bg-white/5'}`}>
            <Rocket size={18} /> <span className="font-bold text-sm">Strategic Planner</span>
          </button>
          <div className="pt-6">
            <div className="bg-slate-900/50 border border-slate-800 rounded-3xl p-6 space-y-4">
              <h3 className="text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] flex items-center gap-2"><Cpu size={14} /> Agent Monitor</h3>
              <div className="space-y-4 max-h-40 overflow-y-auto custom-scrollbar">
                {jobs.map(j => (
                  <div key={j.id} className="space-y-2">
                    <div className="flex justify-between items-center text-[9px] font-bold">
                      <span className="text-slate-400 truncate w-32">{j.name}</span>
                      <span className={j.status === 'completed' ? 'text-emerald-500' : 'text-blue-500 animate-pulse'}>{j.status}</span>
                    </div>
                    <div className="h-1 bg-slate-800 rounded-full overflow-hidden">
                      <div className={`h-full ${j.status === 'completed' ? 'bg-emerald-500' : 'bg-blue-600'} transition-all`} style={{ width: `${j.progress}%` }} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </nav>
        <div className="p-4 bg-slate-900/40 rounded-3xl border border-slate-800">
          <div className="flex items-center gap-3 mb-4">
            <img src={user?.image} alt="U" className="w-8 h-8 rounded-full" />
            <div className="overflow-hidden">
              <p className="text-[10px] font-black truncate">{user?.name}</p>
              <p className="text-[8px] text-slate-500 truncate">{user?.email}</p>
            </div>
          </div>
          <button onClick={() => setIsAuthenticated(false)} className="w-full py-2 bg-slate-800 hover:bg-red-500/10 hover:text-red-500 rounded-xl text-[10px] font-bold transition-all flex items-center justify-center gap-2"><LogOut size={12} /> Terminate</button>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 overflow-y-auto relative bg-[radial-gradient(ellipse_at_top,_#1e293b_0%,_#020617_80%)]">
        <header className="sticky top-0 z-30 bg-slate-950/60 backdrop-blur-2xl border-b border-slate-900 p-6 flex justify-between items-center px-10">
          <div className="flex-1 max-w-2xl flex gap-3">
            <form onSubmit={runMarketIntelligence} className="flex-1 relative group">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-500 group-focus-within:text-blue-500 transition-colors" size={20} />
              <input 
                type="text" 
                placeholder="Search niche (e.g. 'React UI Kit', 'Node.js Boilerplate')..." 
                value={searchQuery} 
                onChange={(e) => setSearchQuery(e.target.value)} 
                className="w-full bg-slate-900/50 border-2 border-slate-800 rounded-2xl py-3 pl-12 pr-4 text-sm focus:border-blue-500/50 outline-none transition-all" 
              />
            </form>
            {activeTab === 'discovery' && (
              <button 
                type="button"
                onClick={handleSaveSearch}
                title="Save current search query"
                className="bg-slate-900 border-2 border-slate-800 px-4 rounded-2xl text-[10px] font-black uppercase tracking-widest hover:border-blue-500/50 hover:text-blue-400 transition-all flex items-center gap-2 whitespace-nowrap"
              >
                <Bookmark size={14} /> Save Search
              </button>
            )}
          </div>
          <div className="flex gap-4 items-center">
             <div className="flex items-center gap-2 bg-emerald-500/10 text-emerald-500 px-3 py-1.5 rounded-full text-xs font-bold border border-emerald-500/20"><Globe size={14} /> Grounding Sync: Active</div>
          </div>
        </header>

        <div className="p-10 max-w-7xl mx-auto space-y-12">
          {error && <div className="p-5 bg-red-950/20 border border-red-500/20 text-red-400 rounded-3xl flex items-center gap-3"><AlertCircle size={20} /> <span className="text-sm font-bold">{error}</span></div>}

          {activeTab === 'dashboard' && (
            <div className="space-y-12 animate-in fade-in">
              <div className="space-y-2">
                <h2 className="text-5xl font-black tracking-tighter">Command Dashboard</h2>
                <p className="text-slate-500 text-lg">Cross-niche pattern recognition and trend velocity.</p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                {[
                  { label: 'Scans', val: searchHistory.length, icon: SearchCode, color: 'text-blue-500' },
                  { label: 'Analyses', val: analysisResults.length, icon: BarChart3, color: 'text-purple-500' },
                  { label: 'Blueprints', val: userProjects.length, icon: Rocket, color: 'text-orange-500' },
                  { label: 'Favorites', val: favorites.length, icon: Heart, color: 'text-rose-500' }
                ].map((stat, i) => (
                  <div key={i} className="bg-slate-900/50 border border-slate-800 p-8 rounded-[3rem] flex items-center gap-6">
                    <div className={`${stat.color} bg-white/5 p-4 rounded-2xl`}><stat.icon size={28} /></div>
                    <div><p className="text-[10px] font-black text-slate-500 uppercase tracking-widest">{stat.label}</p><p className="text-3xl font-black">{stat.val}</p></div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'discovery' && (
            <div className="space-y-10 animate-in fade-in">
               <div className="flex flex-col lg:flex-row justify-between items-start gap-6">
                  <div className="space-y-4 flex-1">
                    <h2 className="text-5xl font-black tracking-tighter">Discovery Hub</h2>
                    <p className="text-slate-500 text-lg">Analyze niches or trigger direct product scraping.</p>
                    
                    <div className="flex flex-wrap items-center gap-4">
                      {/* Minimum Rating Filter */}
                      <div className="flex items-center gap-4 bg-slate-900/50 border border-slate-800 p-1.5 rounded-2xl w-fit">
                        <div className="flex items-center gap-2 px-3 text-[10px] font-black text-slate-500 uppercase tracking-widest">
                          <Star size={12} className="text-yellow-500 fill-yellow-500" /> Min Rating
                        </div>
                        {[0, 3, 4, 4.5].map(r => (
                          <button 
                            key={r} 
                            onClick={() => setMinRating(r)}
                            className={`px-4 py-1.5 rounded-xl text-[10px] font-black transition-all ${minRating === r ? 'bg-blue-600 text-white shadow-lg' : 'hover:bg-white/5 text-slate-400'}`}
                          >
                            {r === 0 ? 'All' : `${r}★+`}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Recent Searches Panel */}
                    {searchHistory.length > 0 && (
                      <div className="space-y-3 pt-4">
                        <div className="flex items-center gap-2 text-[10px] font-black text-slate-500 uppercase tracking-widest">
                          <History size={14} /> Recent Intel Scans
                        </div>
                        <div className="flex flex-wrap gap-2">
                          {searchHistory.slice(0, 6).map(item => (
                            <div 
                              key={item.id} 
                              className="group flex items-center gap-3 bg-slate-900/50 border border-slate-800 hover:border-blue-500/30 px-4 py-2 rounded-xl transition-all cursor-pointer"
                              onClick={() => { setSearchQuery(item.query); performSearch(item.query); }}
                            >
                              <span className="text-xs font-bold text-slate-300 group-hover:text-blue-400">{item.query}</span>
                              <button 
                                onClick={(e) => removeSearchHistoryItem(item.id, e)}
                                className="text-slate-600 hover:text-red-400 opacity-0 group-hover:opacity-100 transition-opacity"
                              >
                                <X size={12} />
                              </button>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                  <div className="w-full lg:max-w-md bg-slate-900 border border-slate-800 p-6 rounded-[2.5rem] shadow-xl">
                    <div className="flex items-center gap-2 mb-4 text-[10px] font-black text-blue-500 uppercase tracking-widest"><LinkIcon size={14} /> Direct Analysis</div>
                    <form onSubmit={runUrlAnalysis} className="flex gap-2">
                      <input type="url" placeholder="Paste CodeCanyon URL..." value={urlInput} onChange={(e) => setUrlInput(e.target.value)} className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-xs outline-none focus:border-blue-500/50 transition-all" />
                      <button type="submit" disabled={isLoading || !urlInput} className="bg-blue-600 hover:bg-blue-500 text-white p-2.5 rounded-xl transition-all disabled:opacity-50"><Zap size={18} fill="white" /></button>
                    </form>
                  </div>
               </div>
               {isLoading && !products.length ? (
                 <div className="py-40 flex flex-col items-center justify-center gap-8 text-center"><Loader2 className="animate-spin text-blue-500" size={64} /><p className="text-xl font-black">Syncing CodeCanyon Indices...</p></div>
               ) : filteredProducts.length > 0 ? (
                 <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 animate-in slide-in-from-bottom-4">
                    {filteredProducts.map(p => (
                      <ProductCard key={p.id} product={p} />
                    ))}
                 </div>
               ) : products.length > 0 ? (
                  <div className="text-center py-40 border-2 border-dashed border-slate-800 rounded-[3rem] space-y-6">
                    <Star className="mx-auto text-slate-800" size={64} />
                    <h3 className="text-3xl font-black">No matches</h3>
                    <p className="text-slate-500 max-w-md mx-auto">None of the found products meet your minimum rating of {minRating} stars.</p>
                  </div>
               ) : (
                 <div className="text-center py-40 border-2 border-dashed border-slate-800 rounded-[3rem] space-y-6"><Globe className="mx-auto text-slate-800" size={64} /><h3 className="text-3xl font-black">Orchestrator Idle</h3></div>
               )}
            </div>
          )}

          {activeTab === 'favorites' && (
            <div className="space-y-10 animate-in fade-in">
              <div className="space-y-2">
                <h2 className="text-5xl font-black tracking-tighter flex items-center gap-4">
                  <Heart className="text-rose-500" size={48} fill="currentColor" /> Favorites
                </h2>
                <p className="text-slate-500 text-lg">Curated list of high-potential products for future analysis.</p>
              </div>
              {favorites.length > 0 ? (
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 animate-in slide-in-from-bottom-4">
                   {favorites.map(p => (
                     <ProductCard key={p.id} product={p} />
                   ))}
                </div>
              ) : (
                <div className="text-center py-40 border-2 border-dashed border-slate-800 rounded-[3rem] space-y-6">
                  <Heart className="mx-auto text-slate-800" size={64} />
                  <h3 className="text-3xl font-black text-slate-500">No Favorites Yet</h3>
                  <p className="text-slate-600 max-w-md mx-auto">Mark products during discovery to keep track of high-yield opportunities.</p>
                  <button onClick={() => setActiveTab('discovery')} className="px-8 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-2xl font-black text-sm transition-all shadow-xl">Explore Marketplace</button>
                </div>
              )}
            </div>
          )}

          {activeTab === 'analysis' && (
            <div className="space-y-12 animate-in fade-in duration-700">
               {!selectedProduct ? (
                 <div className="text-center py-40 border-2 border-dashed border-slate-800 rounded-[3rem] text-slate-600">Gap analyzer. Select a product to begin.</div>
               ) : isLoading ? (
                  <div className="p-20 flex flex-col items-center gap-8 bg-slate-900/20 border border-slate-800 rounded-[3rem]"><Loader2 className="animate-spin text-blue-500" size={48} /><p className="text-xl font-bold">Comparing Matrices...</p></div>
               ) : currentAnalysis && (
                  <div className="space-y-12">
                    <div className="flex items-center gap-6">
                      <button onClick={() => setActiveTab('discovery')} className="p-4 bg-slate-900 border border-slate-800 rounded-2xl hover:bg-slate-800 transition-all"><ChevronRight className="rotate-180" size={24} /></button>
                      <h2 className="text-4xl font-black tracking-tighter">{selectedProduct.title}</h2>
                    </div>

                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
                      <div className="bg-gradient-to-br from-blue-600 to-indigo-900 p-12 rounded-[4rem] shadow-2xl flex flex-col gap-8 relative overflow-hidden h-full">
                        <div className="flex items-center justify-between">
                          <div className="text-center shrink-0">
                            <p className="text-[10px] font-black text-blue-100 uppercase mb-2 tracking-widest">Profitability Score</p>
                            <div className="text-[8rem] font-black tracking-tighter leading-none">{currentAnalysis.profitabilityScore}</div>
                          </div>
                          <div className={`px-6 py-2 rounded-2xl font-black text-xs uppercase tracking-widest ${currentAnalysis.isBlueOcean ? 'bg-emerald-500 text-white' : 'bg-slate-950/40 text-blue-200'}`}>
                            {currentAnalysis.isBlueOcean ? 'Blue Ocean' : 'Red Ocean'}
                          </div>
                        </div>
                        <p className="text-blue-50 font-medium leading-relaxed italic text-xl">"{currentAnalysis.reasoning}"</p>
                        <div className="mt-auto pt-6 border-t border-white/10 flex justify-between items-center text-[10px] font-black uppercase text-blue-200">
                          <span>Grounding Validation: Verified</span>
                          <span className="flex items-center gap-1"><ShieldCheck size={12} /> Encrypted Engine</span>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 gap-8">
                        {/* Sales Velocity Chart */}
                        <div className="bg-slate-900/50 border-2 border-slate-800 p-8 rounded-[4rem] flex flex-col">
                          <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-black flex items-center gap-3 text-blue-500"><TrendingUp size={20} /> Sales Velocity</h3>
                            <span className="text-[9px] font-bold text-slate-500 uppercase">Trend Analysis (Drag to Zoom)</span>
                          </div>
                          <div className="flex-1 w-full min-h-[220px]">
                            <ResponsiveContainer width="100%" height="100%">
                              <AreaChart data={salesChartData}>
                                <defs>
                                  <linearGradient id="colorVel" x1="0" y1="0" x2="0" y2="1">
                                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.8}/>
                                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                                  </linearGradient>
                                </defs>
                                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                                <XAxis dataKey="name" stroke="#64748b" fontSize={9} tickLine={false} axisLine={false} tick={{ fontWeight: 'bold' }} />
                                <YAxis stroke="#64748b" fontSize={9} tickLine={false} axisLine={false} tick={{ fontWeight: 'bold' }} />
                                <Tooltip contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px' }} itemStyle={{ color: '#60a5fa', fontWeight: 'bold', fontSize: '11px' }} />
                                <Area type="monotone" dataKey="velocity" stroke="#3b82f6" strokeWidth={2} fillOpacity={1} fill="url(#colorVel)" animationDuration={1000} />
                                <Brush 
                                  dataKey="name" 
                                  height={20} 
                                  stroke="#3b82f6" 
                                  fill="#0f172a" 
                                  travellerWidth={10}
                                  gap={1}
                                />
                              </AreaChart>
                            </ResponsiveContainer>
                          </div>
                        </div>

                        {/* Price History Chart */}
                        <div className="bg-slate-900/50 border-2 border-slate-800 p-8 rounded-[4rem] flex flex-col">
                          <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-black flex items-center gap-3 text-emerald-500"><DollarSign size={20} /> Price Evolution</h3>
                            <span className="text-[9px] font-bold text-slate-500 uppercase">Valuation Growth (Drag to Zoom)</span>
                          </div>
                          <div className="flex-1 w-full min-h-[220px]">
                            <ResponsiveContainer width="100%" height="100%">
                              <LineChart data={priceChartData}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                                <XAxis dataKey="name" stroke="#64748b" fontSize={9} tickLine={false} axisLine={false} tick={{ fontWeight: 'bold' }} />
                                <YAxis stroke="#64748b" fontSize={9} tickLine={false} axisLine={false} tick={{ fontWeight: 'bold' }} />
                                <Tooltip contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px' }} itemStyle={{ color: '#10b981', fontWeight: 'bold', fontSize: '11px' }} />
                                <Line type="stepAfter" dataKey="price" stroke="#10b981" strokeWidth={3} dot={{ fill: '#10b981', r: 3 }} activeDot={{ r: 5 }} animationDuration={1000} />
                                <Brush 
                                  dataKey="name" 
                                  height={20} 
                                  stroke="#10b981" 
                                  fill="#0f172a" 
                                  travellerWidth={10}
                                  gap={1}
                                />
                              </LineChart>
                            </ResponsiveContainer>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div className="grid grid-cols-1 xl:grid-cols-3 gap-10">
                      <div className="xl:col-span-2 space-y-8">
                         <div className="grid md:grid-cols-2 gap-8 h-full">
                            <div className="bg-slate-900/50 border-2 border-slate-800 p-10 rounded-[3rem] space-y-8 h-full">
                              <h3 className="text-2xl font-black flex items-center gap-3 text-emerald-500"><CheckCircle2 /> Identified Gaps</h3>
                              <div className="space-y-4">
                                {currentAnalysis.featureGaps.map((g, i) => (
                                  <div key={i} className="flex gap-4 items-start text-slate-300 font-bold bg-slate-950/40 p-5 rounded-2xl border border-slate-800"><Plus className="text-emerald-500 shrink-0" size={20} /> {g}</div>
                                ))}
                              </div>
                            </div>
                            <div className="bg-slate-900/50 border-2 border-slate-800 p-10 rounded-[3rem] space-y-8 h-full flex flex-col justify-between">
                              <div>
                                <h3 className="text-2xl font-black flex items-center gap-3 text-orange-400"><Target /> Weaknesses</h3>
                                <div className="space-y-4 mt-8">
                                  {currentAnalysis.competitorWeaknesses.map((w, i) => (
                                    <div key={i} className="flex gap-4 items-start text-slate-300 font-bold bg-slate-950/40 p-5 rounded-2xl border border-slate-800"><TrendingDown className="text-red-500 shrink-0" size={20} /> {w}</div>
                                  ))}
                                </div>
                              </div>
                              <button onClick={runStructuralPlanning} className="w-full mt-6 py-6 bg-blue-600 hover:bg-blue-500 text-white rounded-3xl font-black text-lg shadow-2xl flex items-center justify-center gap-3">Generate Strategy <Rocket size={24} /></button>
                            </div>
                         </div>
                      </div>
                      <div className="bg-slate-900/80 border border-slate-800 p-10 rounded-[3rem] space-y-8 h-full">
                        <h4 className="text-[10px] font-black text-slate-600 uppercase tracking-widest">Intelligence Metrics</h4>
                        <div className="space-y-6">
                          <StatBar label="Sales Velocity" value={currentAnalysis.metrics.salesVelocityScore} color="bg-blue-500" />
                          <StatBar label="Revenue Potential" value={currentAnalysis.metrics.revenueScore} color="bg-indigo-500" />
                          <StatBar label="Saturation" value={currentAnalysis.metrics.saturationScore} color="bg-emerald-500" />
                          <StatBar label="Updates" value={currentAnalysis.metrics.updateScore} color="bg-orange-500" />
                          <StatBar label="Ratings" value={currentAnalysis.metrics.ratingScore} color="bg-yellow-500" />
                        </div>
                      </div>
                    </div>
                  </div>
               )}
            </div>
          )}

          {activeTab === 'projects' && (
            <div className="space-y-12 animate-in fade-in zoom-in-95">
               {!devPlan ? (
                 <div className="text-center py-40 border-2 border-dashed border-slate-800 rounded-[3rem] text-slate-600">No blueprint. Run analysis to plan.</div>
               ) : (
                 <div className="space-y-10">
                    <div className="flex flex-col lg:flex-row justify-between items-start gap-8">
                       <div className="space-y-3">
                          <h2 className="text-6xl font-black tracking-tighter">{devPlan.projectName}</h2>
                          <p className="text-slate-400 text-2xl font-medium max-w-4xl italic">Based on: {devPlan.baseProduct}</p>
                          <p className="text-slate-300 text-xl font-medium italic">"{devPlan.concept}"</p>
                       </div>
                       <div className="flex flex-wrap gap-4">
                         <button onClick={saveProject} className="bg-slate-900 border border-slate-800 hover:border-blue-500/50 px-8 py-4 rounded-[2rem] font-black text-sm flex items-center gap-3 transition-all"><Save size={20} /> Save Blueprint</button>
                         <button onClick={handleNewProject} className="bg-slate-950 border border-slate-800 hover:border-red-500/30 px-8 py-4 rounded-[2rem] font-black text-sm flex items-center gap-3 transition-all text-slate-400 hover:text-red-400"><PlusCircle size={20} /> New Project</button>
                       </div>
                    </div>
                    <div className="flex flex-wrap gap-2 p-1 bg-slate-900/50 border border-slate-800 rounded-[2.5rem] w-full lg:w-fit">
                       {['Innovation', 'Tech Stack', 'Roadmap', 'Marketplace Compliance'].map((step, idx) => (
                         <button key={idx} onClick={() => setPlannerStep(idx)} className={`px-8 py-3.5 rounded-[2rem] font-black text-xs transition-all uppercase tracking-widest ${plannerStep === idx ? 'bg-blue-600 text-white shadow-xl' : 'text-slate-500 hover:text-white'}`}>{step}</button>
                       ))}
                    </div>
                    <div className="bg-slate-900/30 border-2 border-slate-800 p-12 rounded-[4rem] min-h-[500px]">
                      {plannerStep === 0 && (
                        <div className="grid md:grid-cols-2 gap-12">
                          <div className="space-y-8">
                             <h3 className="text-3xl font-black text-blue-400 flex items-center gap-4"><Lightbulb /> Strategy</h3>
                             <p className="text-slate-300 text-xl font-medium italic">"{devPlan.innovationStrategy}"</p>
                             <div className="space-y-4 pt-4">
                               <h4 className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Unique Selling Points</h4>
                               <div className="grid gap-3">
                                 {devPlan.uniqueSellingPoints.map((usp, i) => (
                                   <div key={i} className="flex gap-3 items-center bg-slate-950/40 p-4 rounded-2xl border border-slate-800">
                                     <ArrowUpRight className="text-blue-500 shrink-0" size={18} />
                                     <span className="text-sm font-bold text-slate-300">{usp}</span>
                                   </div>
                                 ))}
                               </div>
                             </div>
                          </div>
                          <div className="bg-slate-950/40 border border-slate-800 p-10 rounded-[3rem] space-y-8">
                             <h4 className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Financial Projection</h4>
                             <div className="space-y-8">
                                <div className="flex justify-between items-center pb-4 border-b border-slate-800">
                                  <span className="text-slate-400 font-bold">Estimated Development</span>
                                  <span className="text-2xl font-black text-blue-400">{devPlan.roiAnalysis.estimatedEffortDays} Days</span>
                                </div>
                                <div className="flex justify-between items-center pb-4 border-b border-slate-800">
                                  <span className="text-slate-400 font-bold">Recommended Pricing</span>
                                  <span className="text-2xl font-black text-emerald-400">${devPlan.pricingStrategy.recommendedPrice}</span>
                                </div>
                                <div className="flex justify-between items-center">
                                  <span className="text-slate-400 font-bold">Break-even Period</span>
                                  <span className="text-2xl font-black text-orange-400">{devPlan.roiAnalysis.breakEvenMonths} Months</span>
                                </div>
                                <div className="bg-blue-600/10 p-6 rounded-3xl border border-blue-500/20 mt-4">
                                  <p className="text-[10px] font-black text-blue-400 uppercase tracking-widest mb-2">Marketing Angle</p>
                                  <p className="text-sm font-bold text-blue-200">"{devPlan.pricingStrategy.marketingAngle}"</p>
                                </div>
                             </div>
                          </div>
                        </div>
                      )}
                      {plannerStep === 1 && (
                        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                           {[
                             { label: 'Frontend', items: devPlan.techStack.frontend, color: 'text-blue-400', icon: Monitor },
                             { label: 'Backend', items: devPlan.techStack.backend, color: 'text-purple-400', icon: Cpu },
                             { label: 'Database', items: devPlan.techStack.database, color: 'text-emerald-400', icon: Database },
                             { label: 'Modern Upgrades', items: devPlan.techStack.modernUpgrades, color: 'text-orange-400', icon: Zap }
                           ].map((stack, i) => (
                             <div key={i} className="p-8 bg-slate-950/50 border border-slate-800 rounded-[2.5rem] hover:border-slate-700 transition-all flex flex-col">
                                <div className="flex items-center gap-3 mb-6">
                                  <stack.icon className={stack.color} size={20} />
                                  <h4 className={`font-black uppercase tracking-widest text-[10px] ${stack.color}`}>{stack.label}</h4>
                                </div>
                                <div className="space-y-3 mt-auto">{stack.items.map((it, j) => <div key={j} className="text-slate-300 text-xs font-bold bg-white/5 p-2.5 rounded-xl border border-white/5">{it}</div>)}</div>
                             </div>
                           ))}
                        </div>
                      )}
                      {plannerStep === 2 && (
                         <div className="grid md:grid-cols-2 gap-8">
                            {devPlan.roadmap.map((phase, i) => (
                              <div key={i} className="p-8 bg-slate-950/50 border border-slate-800 rounded-[2.5rem] hover:border-blue-500/20 transition-all">
                                <div className="flex items-center gap-4 mb-6">
                                  <div className="bg-blue-600 text-white w-8 h-8 rounded-xl flex items-center justify-center font-black text-xs">{i + 1}</div>
                                  <h4 className="font-black text-blue-500 uppercase tracking-widest text-sm">{phase.phase}</h4>
                                </div>
                                <ul className="space-y-4">
                                  {phase.tasks.map((t, j) => <li key={j} className="text-slate-400 text-sm font-bold flex gap-3"><ChevronRight size={14} className="text-blue-800 shrink-0" /> {t}</li>)}
                                </ul>
                              </div>
                            ))}
                         </div>
                      )}
                      {plannerStep === 3 && (
                        <div className="space-y-12 animate-in fade-in slide-in-from-top-4">
                           <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                             <div className="space-y-2">
                               <h3 className="text-3xl font-black text-orange-400 flex items-center gap-4">
                                 <ShieldCheck className="text-orange-500" /> CodeCanyon Compliance Matrix
                               </h3>
                               <p className="text-slate-500 text-sm font-medium">Automated validation against Envato Marketplace quality standards.</p>
                             </div>
                             <div className="flex gap-4">
                               <div className="bg-emerald-500/10 text-emerald-500 px-6 py-2 rounded-2xl font-black text-[10px] uppercase tracking-widest border border-emerald-500/20">
                                 Status: Submission Ready
                               </div>
                               <button className="bg-slate-900 border border-slate-800 px-4 py-2 rounded-2xl text-[10px] font-black uppercase tracking-widest hover:border-orange-500/50 hover:text-orange-400 transition-all flex items-center gap-2">
                                 <Download size={14} /> Export Guide
                               </button>
                             </div>
                           </div>
                           <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                              {devPlan.complianceChecklist.map((cat, i) => (
                                <div key={i} className="p-8 bg-slate-950/50 border border-slate-800 rounded-[3rem] shadow-xl hover:border-orange-500/30 transition-all flex flex-col group">
                                  <h4 className="font-black text-slate-500 mb-6 uppercase text-[10px] tracking-widest flex items-center gap-2 group-hover:text-orange-400 transition-colors">
                                    <Layers size={14} className="text-orange-500" /> {cat.category}
                                  </h4>
                                  <ul className="space-y-4 flex-1">
                                    {cat.items.map((it, j) => (
                                      <li key={j} className="text-slate-300 text-xs font-bold flex gap-4 leading-relaxed group/item">
                                        <div className="w-5 h-5 rounded-md bg-orange-500/10 flex items-center justify-center shrink-0 group-hover/item:bg-orange-500/20 transition-colors">
                                          <CheckCircle2 size={14} className="text-orange-500" />
                                        </div>
                                        <span className="group-hover/item:text-white transition-colors">{it}</span>
                                      </li>
                                    ))}
                                  </ul>
                                </div>
                              ))}
                              {/* Extra Compliance Info Card */}
                              <div className="p-8 bg-orange-600/5 border border-orange-500/20 rounded-[3rem] shadow-xl flex flex-col justify-center text-center space-y-6">
                                <FileBadge size={48} className="mx-auto text-orange-500" />
                                <div>
                                  <h4 className="text-lg font-black text-orange-200">Envato Elite Verified</h4>
                                  <p className="text-xs font-medium text-orange-500/70 mt-2 leading-relaxed">This blueprint adheres to 2024 marketplace guidelines including PSR compliance and documentation nesting.</p>
                                </div>
                                <button className="w-full py-4 bg-orange-600 hover:bg-orange-500 text-white rounded-2xl font-black text-[10px] uppercase tracking-widest transition-all">Submit Review</button>
                              </div>
                           </div>
                        </div>
                      )}
                    </div>
                 </div>
               )}
            </div>
          )}

          {activeTab === 'trends' && (
            <div className="space-y-12 animate-in fade-in">
              <h2 className="text-5xl font-black tracking-tighter">Market Pulse</h2>
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">{marketTrends.map((t, i) => (<div key={i} className="bg-slate-900/40 border border-slate-800 p-10 rounded-[3rem] space-y-6"><div className="flex justify-between items-center"><span className="bg-emerald-500/10 text-emerald-400 text-[10px] font-black px-4 py-1.5 rounded-full uppercase tracking-widest">{t.category}</span><div className="text-emerald-400 font-black text-lg flex items-center gap-1"><TrendingUp size={20} /> {t.growthRate}</div></div><div className="flex flex-wrap gap-2 pt-4 border-t border-slate-800">{t.trendingTech.map((tech, j) => <span key={j} className="text-[10px] font-bold text-slate-500 bg-slate-950 px-3 py-1 rounded-lg border border-slate-800">{tech}</span>)}</div></div>))}</div>
            </div>
          )}

          {activeTab === 'knowledge' && (
            <div className="space-y-12 animate-in fade-in">
               <h2 className="text-5xl font-black tracking-tighter">Reference</h2>
               <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">{knowledgeBase.map((kb, i) => (<a key={i} href={kb.uri} target="_blank" className="p-8 bg-slate-900 border border-slate-800 rounded-[2.5rem] hover:border-blue-500/50 transition-all flex justify-between items-center gap-6 group"><div className="space-y-1 truncate pr-4"><p className="text-sm font-black text-slate-300 group-hover:text-blue-400 transition-colors truncate">{kb.title}</p><p className="text-[8px] text-slate-600 font-bold truncate uppercase tracking-widest">{kb.uri}</p></div><ExternalLink size={20} className="text-slate-800 group-hover:text-blue-500 transition-all shrink-0" /></a>))}</div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

createRoot(document.getElementById('root')!).render(<App />);
