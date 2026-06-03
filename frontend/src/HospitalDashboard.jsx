// hospitalDashboard.jsx
import React, { useState, useEffect } from "react";
import hospitalLogo from "./assets/hospital_logo.png";
import companyLogo from "./assets/company_logo.png";

import {
    Users,
    User,
    Shield,
    PieChart as PieChartIcon,
    BarChart3,
    Activity,
    ClipboardList,
    Bed,
    RefreshCw,
    Calendar,
} from "lucide-react";

import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    Legend,
    ResponsiveContainer,
    CartesianGrid,
    PieChart as RechartsPieChart,
    Pie,
    Cell,
} from "recharts";

export default function HospitalDashboard() {
    const [settings, setSettings] = useState(null);
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const [fromDate, setFromDate] = useState("");
    const [toDate, setToDate] = useState("");
    const [selectedPreset, setSelectedPreset] = useState("today");

    const [autoRefresh, setAutoRefresh] = useState(true);
    const [refreshSeconds, setRefreshSeconds] = useState(30);
    const [lastUpdated, setLastUpdated] = useState("");

    // 2. Define the function that fetches data from Django
    const fetchDashboardData = (from = fromDate, to = toDate, silent = false) => {
        if (!silent) {
            setLoading(true);
        }

        const params = new URLSearchParams();

        if (from && to) {
            params.append("from_date", from);
            params.append("to_date", to);
        }

        const url = `/dash/?${params.toString()}`;

        // Replace with your actual Django server URL if different
        fetch(url)
            .then(async (response) => {
                const text = await response.text();

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${text}`);
                }

                try {
                    return JSON.parse(text);
                } catch {
                    console.error("Django returned non-JSON:", text);
                    throw new Error("Django returned HTML/text instead of JSON");
                }
            })
            .then((jsonData) => {
                setData(jsonData);
                setLastUpdated(new Date().toLocaleTimeString());
                setLoading(false);
            })
            .catch((err) => {
                console.error("Error fetching data:", err);
                setError(err.message);
                setLoading(false);
            });
    };

    // 3. Run the fetch function automatically when the component mounts
    useEffect(() => {
        fetch("/dash/settings/")
            .then(async (res) => {
                const text = await res.text();
                try {
                    return JSON.parse(text);
                } catch {
                    console.error("Settings returned non-JSON:", text);
                    return null;
                }
            })
            .then((data) => {
                if (data) setSettings(data);
            })
            .catch((err) => console.error("Settings fetch error:", err));
    }, []);

    useEffect(() => {
        fetchDashboardData();
    }, []);

    useEffect(() => {
        if (!autoRefresh) return;

        const intervalId = setInterval(() => {
            fetchDashboardData(fromDate, toDate, true);
        }, refreshSeconds * 1000);

        return () => clearInterval(intervalId);
    }, [autoRefresh, refreshSeconds, fromDate, toDate]);

    // 4. Handle Loading State
    if (loading) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-slate-100">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-900 mb-4"></div>
                <p className="text-slate-600 font-bold animate-pulse">Synchronizing HMIS Analytics Hub...</p>
            </div>
        );
    }

    // 5. Handle Error State
    if (error) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-slate-100 p-4">
                <div className="bg-red-50 border border-red-200 text-red-700 px-6 py-4 rounded-xl shadow-sm text-center">
                    <h3 className="font-bold text-lg mb-1">Connection Error</h3>
                    <p className="text-sm mb-4">{error}</p>
                    <button
                        onClick={fetchDashboardData}
                        className="bg-red-600 hover:bg-red-700 text-white font-bold text-xs px-4 py-2 rounded-lg transition"
                    >
                        Retry Connection
                    </button>
                </div>
            </div>
        );
    }

    const formatDate = (date) => {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, "0");
        const day = String(date.getDate()).padStart(2, "0");
        return `${year}-${month}-${day}`;
    };

    const applyDatePreset = (preset) => {
        const today = new Date();
        let from = new Date();
        let to = new Date();

        if (preset === "today") {
            from = today;
            to = today;
        } else if (preset === "yesterday") {
            from.setDate(today.getDate() - 1);
            to.setDate(today.getDate() - 1);
        } else if (preset === "this_week") {
            const day = today.getDay();
            const diffToMonday = day === 0 ? -6 : 1 - day;
            from.setDate(today.getDate() + diffToMonday);
            to = today;
        } else if (preset === "last_7_days") {
            from.setDate(today.getDate() - 6);
            to = today;
        } else if (preset === "this_month") {
            from = new Date(today.getFullYear(), today.getMonth(), 1);
            to = today;
        }

        const formattedFrom = formatDate(from);
        const formattedTo = formatDate(to);

        setFromDate(formattedFrom);
        setToDate(formattedTo);
        setSelectedPreset(preset);

        fetchDashboardData(formattedFrom, formattedTo);
    };

    const paymentChartData = Object.entries(data.paymentTypes || {}).map(([key, value]) => ({
        name: key,
        total: value.count || 0,
        female: value.female ?? value.Female ?? 0,
        male: value.male ?? value.Male ?? 0,
        percentage: value.percentage ?? value.Percentage ?? 0,
    }));
    const paymentPieData = Object.entries(data.paymentTypes || {}).map(([key, value]) => ({
        name: key,
        value: value.count || 0,
        percentage: value.percentage ?? value.Percentage ?? 0,
    }));
    const COLORS = ["#2563eb", "#10b981", "#f97316", "#a855f7", "#ef4444"];
    const PaymentTypePatPieData = () => (
        <div className="w-full h-80">
            <ResponsiveContainer width="100%" height="100%">
                <RechartsPieChart>
                    <text
                        x="50%"
                        y="48%"
                        textAnchor="middle"
                        dominantBaseline="middle"
                        className="fill-slate-900 text-4xl font-black"
                    >
                        {data.demographics.total}
                    </text>

                    <text
                        x="50%"
                        y="58%"
                        textAnchor="middle"
                        dominantBaseline="middle"
                        className="fill-slate-500 text-xs font-bold"
                    >
                        Total Patients
                    </text>
                    <Pie
                        data={paymentPieData}
                        dataKey="value"
                        nameKey="name"
                        outerRadius="80%"
                        innerRadius="55%"
                        paddingAngle={3}
                        isAnimationActive={true}
                        label={({ percentage }) => `${percentage}%`}
                    >
                        {paymentPieData.map((entry, index) => (
                            <Cell
                                key={`cell-${index}`}
                                fill={COLORS[index % COLORS.length]}
                            />
                        ))}
                    </Pie>

                    <Tooltip
                        formatter={(value, name) => [`${value} patients`, name]}
                    />

                    <Legend wrapperStyle={{ fontSize: "11px" }} />
                </RechartsPieChart>
            </ResponsiveContainer>
        </div>
    );

    // DepartmentWise Consultation
    const consultationRows = Object.entries(data.consultations || {}).map(([dept, value]) => ({
        name: dept,
        count: value.count || 0,
        female: value.female ?? value.Female ?? 0,
        male: value.male ?? value.Male ?? 0,
        unknown: value.unknown ?? value.Unknown ?? 0,
        percentage: value.percentage ?? value.Percentage ?? 0,
    }));
    //Departmentwise Bed Occupancy
    // const bedoccupancy = Object.entries(data.beds || {}).map(([value]) => ({
    //     dept: value.name || 0,
    //     total: value.total || 0,
    //     occupied: value.occupied || 0,
    //     vacant: value.vacant || 0,
    //     pct: value.pct || 0
    // }))
    const totalDiagnostics = data.diagnostics.reduce(
        (sum, item) => sum + Number(item.count || 0),
        0
    );

    const totalConsultations = consultationRows.reduce(
        (sum, item) => sum + Number(item.count || 0),
        0
    );

    const totalBeds = data.beds.reduce((sum, item) => sum + Number(item.total || 0), 0);
    const totalOccupied = data.beds.reduce((sum, item) => sum + Number(item.occupied || 0), 0);
    const overallOccupancy = totalBeds ? Math.round((totalOccupied / totalBeds) * 100) : 0;
    // 6. Render the Dashboard once data is loaded successfully
    return (
        <div className="w-full min-h-screen bg-slate-100 p-2 font-sans text-slate-800 antialiased">
            <div className="w-full border-4 border-blue-700 rounded-xl bg-white p-2">
                {/* --- TOP BAR / HEADER --- */}
                <header className="bg-white rounded-lg shadow-sm p-4 mb-3 grid grid-cols-1 lg:grid-cols-[1fr_auto_auto] items-center gap-6">
                    <div className="flex items-center gap-4">
                        <img
                            src={settings?.hospital_logo || hospitalLogo}
                            alt="Hospital Logo"
                            className="w-20 h-16 object-contain border-0 border-blue-900"
                        />
                        <div>
                            <h1 className="text-2xl md:text-3xl leading-tight text-left font-black tracking-tight text-blue-900">
                                {settings?.hospital_name || "ABC Hospital"}
                            </h1>
                            <p className="text-xs italic text-left font-medium text-emerald-600">Excellence in Care, Every Time</p>
                        </div>
                    </div>

                    {/* Date Filter Controls */}
                    <div className="flex flex-col items-end gap-3 text-xs">

                        <div className="flex flex-col">
                            <span className="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1">
                                Quick Filter
                            </span>

                            <div className="flex flex-wrap gap-2">
                                {[
                                    { key: "today", label: "Today" },
                                    { key: "yesterday", label: "Yesterday" },
                                    { key: "this_week", label: "This Week" },
                                    { key: "last_7_days", label: "Last 7 Days" },
                                    { key: "this_month", label: "This Month" },
                                ].map((item) => (
                                    <button
                                        key={item.key}
                                        onClick={() => applyDatePreset(item.key)}
                                        className={`px-3 py-2 rounded-lg font-bold transition ${selectedPreset === item.key
                                            ? "bg-blue-600 text-white"
                                            : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                                            }`}
                                    >
                                        {item.label}
                                    </button>
                                ))}
                            </div>
                        </div>
                        {/* Row 2: From Date, To Date, Refresh */}
                        <div className="flex flex-wrap items-end gap-3">
                            <div className="flex flex-col">
                                <span className="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1">
                                    From Date
                                </span>

                                <div className="flex items-center gap-2 border rounded-lg px-3 py-2 bg-slate-50">
                                    <Calendar className="w-4 h-4 text-slate-400" />
                                    <input
                                        type="date"
                                        value={fromDate}
                                        onChange={(e) => {
                                            setFromDate(e.target.value);
                                            setSelectedPreset("custom");
                                        }}
                                        className="bg-transparent outline-none font-semibold text-slate-700"
                                    />
                                </div>
                            </div>

                            <div className="flex flex-col">
                                <span className="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1">
                                    To Date
                                </span>

                                <div className="flex items-center gap-2 border rounded-lg px-3 py-2 bg-slate-50">
                                    <Calendar className="w-4 h-4 text-slate-400" />
                                    <input
                                        type="date"
                                        value={toDate}
                                        onChange={(e) => {
                                            setToDate(e.target.value);
                                            setSelectedPreset("custom");
                                        }}
                                        className="bg-transparent outline-none font-semibold text-slate-700"
                                    />
                                </div>
                            </div>

                            <button
                                onClick={() => fetchDashboardData(fromDate, toDate)}
                                className="bg-blue-600 hover:bg-blue-700 transition text-white px-4 py-2 rounded-lg font-bold flex items-center gap-2 shadow-sm shadow-blue-200"
                            >
                                <RefreshCw className="w-3.5 h-3.5" /> Refresh
                            </button>
                        </div>
                        <div className="flex flex-col">
                            <span className="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1">
                                Auto Refresh
                            </span>

                            <div className="flex items-center gap-2">
                                {lastUpdated && (
                                    <span className="text-[10px] text-slate-700 font-bold">
                                        Last Updated: {lastUpdated}
                                    </span>
                                )}
                                <select
                                    value={refreshSeconds}
                                    onChange={(e) => setRefreshSeconds(Number(e.target.value))}
                                    className="border rounded-lg px-3 py-2 bg-slate-50 font-semibold text-slate-700 outline-none"
                                >
                                    <option value={10}>10 sec</option>
                                    <option value={30}>30 sec</option>
                                    <option value={60}>1 min</option>
                                    <option value={300}>5 min</option>
                                </select>

                                <button
                                    onClick={() => setAutoRefresh(!autoRefresh)}
                                    className={`px-3 py-2 rounded-lg font-bold ${autoRefresh
                                        ? "bg-emerald-600 text-white"
                                        : "bg-slate-200 text-slate-600"
                                        }`}
                                >
                                    {autoRefresh ? "ON" : "OFF"}
                                </button>

                            </div>
                        </div>
                    </div>

                    <img
                        src={companyLogo}
                        alt="D-Code Technology Logo"
                        className="w-18 h-16 object-cover border-0 border-blue-900 shadow-sm"
                    />

                </header>

                {/* --- SECTION 1: TOP SUMMARY KPI CARDS --- */}
                <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                    <div className="bg-white rounded-xl p-4 shadow-sm border border-slate-200 flex items-center gap-4">

                        <div className="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-blue"><Users className="w-6 h-6" /></div>
                        <div>
                            <span className="text-xs uppercase font-black text-blue-700">Total Patients</span>
                            <h2 className="text-4xl font-black text-blue-700">{data.demographics.total}</h2>
                            <p className="text-xs text-slate-500 font-semibold">100% of Total Patients</p>

                        </div>
                    </div>

                    <div className="bg-white rounded-xl p-3 shadow-sm border border-slate-200 flex items-center gap-4">

                        <div className="w-16 h-16 rounded-full bg-purple-600 flex items-center justify-center text-purple"><Shield className="w-6 h-6" /></div>
                        <div>
                            <span className="text-xs uppercase font-black text-purple-700">Health Insurance</span>
                            <h2 className="text-4xl font-black text-purple-700">{data.demographics.insuranceCoverage.percentage}%</h2>
                            <p className="text-xs text-slate-500 font-semibold">{data.demographics.insuranceCoverage.count} of {data.demographics.total} Patients</p>
                        </div>

                    </div>

                    <div className="bg-white rounded-xl p-3 shadow-sm border border-slate-200 flex items-center gap-4">

                        <div className="w-16 h-16 rounded-full bg-emerald-600 flex items-center justify-center text-white"><User className="w-6 h-6" /></div>
                        <div>
                            <span className="text-xs uppercase font-black text-emerald-700">Female Patients</span>
                            <h2 className="text-4xl font-black text-emerald-700">{data.demographics.female.count}</h2>
                            <p className="text-xs text-slate-500 font-semibold">{data.demographics.female.percentage}% of Total Patients</p>
                        </div>

                    </div>

                    <div className="bg-white rounded-xl p-3 shadow-sm border border-slate-200 flex items-center gap-4">

                        <div className="w-16 h-16 rounded-full bg-rose-600 flex items-center justify-center text-rose"><User className="w-6 h-6" /></div>
                        <div>
                            <span className="text-xs uppercase font-black text-rose-700">Male Patients</span>
                            <h2 className="text-4xl font-black text-rose-700">{data.demographics.male.count}</h2>
                            <p className="text-xs text-slate-500 font-semibold">{data.demographics.male.percentage}% of Total Patients</p>
                        </div>

                    </div>
                </section>

                {/* --- SECTION 2: PAYMENT TYPE GRAPHICS & METRICS --- */}
                <section className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
                    <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                        <div className="bg-blue-900 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                            <PieChartIcon className="w-4 h-4" /> Patients by Payment Type
                        </div>
                        <div className="p-4 flex flex-col items-center justify-center flex-1">
                            <PaymentTypePatPieData />
                            <div className="w-full space-y-2 text-xs font-semibold mt-4">
                                {paymentPieData.map((item, index) => (
                                    <div key={item.name} className="flex justify-between items-center text-slate-700">
                                        <span>
                                            <span
                                                className="inline-block w-2 h-2 rounded-full mr-2"
                                                style={{ backgroundColor: COLORS[index % COLORS.length] }}
                                            />
                                            {item.name}: {item.value}
                                        </span>
                                        <span>{item.percentage}%</span>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>

                    <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                        <div className="bg-emerald-700 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                            <BarChart3 className="w-4 h-4" /> Patients by Payment Type & Gender
                        </div>
                        <div className="p-4 flex-1 flex flex-col justify-end">
                            <div className="w-full h-80">
                                <ResponsiveContainer width="100%" height="100%">
                                    <BarChart
                                        data={paymentChartData}
                                        margin={{ top: 10, right: 10, left: -20, bottom: 20 }}
                                    >
                                        <Legend wrapperStyle={{ fontSize: "12px" }} />

                                        <Bar dataKey="female" stackId="patients" fill="#10b981" name="Female" />
                                        <Bar dataKey="male" stackId="patients" fill="#f43f5e" name="Male" />
                                        <CartesianGrid strokeDasharray="3 3" vertical={false} />

                                        <XAxis
                                            dataKey="name"
                                            tick={{ fontSize: 10, fontWeight: 1000 }}
                                            angle={-15}
                                            textAnchor="end"
                                            interval={0}
                                        />

                                        <YAxis tick={{ fontSize: 10 }} allowDecimals={false} />

                                        <Tooltip
                                            formatter={(value, name) => {
                                                if (name === "female") return [value, "Female"];
                                                if (name === "male") return [value, "Male"];
                                                if (name === "total") return [value, "Total"];
                                                return [value, name];
                                            }}
                                        />
                                    </BarChart>
                                </ResponsiveContainer>

                            </div>
                        </div>
                    </div>

                    <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                        <div className="bg-orange-600 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                            <ClipboardList className="w-4 h-4" /> Patients by Payment Type (Total)
                        </div>

                        <div className="p-6 space-y-4 flex-1 justify-center flex flex-col">
                            {Object.entries(data.paymentTypes || {}).map(([key, value], index) => {
                                const count = value.count || 0;
                                const percentage = value.percentage ?? value.Percentage ?? 0;

                                const barColors = [
                                    "bg-blue-600",
                                    "bg-emerald-500",
                                    "bg-orange-500",
                                    "bg-purple-500",
                                    "bg-rose-500",
                                ];

                                return (
                                    <div className="flex items-center gap-3" key={key}>
                                        <div className={`${barColors[index % barColors.length]} w-10 h-10 rounded-full flex items-center justify-center text-white`}>
                                            <ClipboardList className="w-5 h-5" />
                                        </div>

                                        <div className="flex-1">
                                            <div className="flex justify-between items-center text-xs font-bold mb-1.5">
                                                <span className="text-slate-700 truncate max-w-[160px]">{key}</span>
                                                <span className="text-slate-900">{count}</span>
                                            </div>

                                            <div className="w-full bg-slate-100 h-3.5 rounded-full overflow-hidden">
                                                <div
                                                    className={`${barColors[index % barColors.length]} h-full rounded-full`}
                                                    style={{ width: `${percentage}%` }}
                                                ></div>
                                            </div>
                                        </div>

                                        <div className="text-right text-xs font-bold text-slate-600 w-12">
                                            {percentage}%
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </section>

                {/* --- SECTION 3: TABULAR LOGISTICS --- */}
                <section className="grid grid-cols-2 lg:grid-cols-3 gap-6">
                    {/* Diagnostic Services */}
                    <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                        <div className="bg-purple-900 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider"><Activity className="w-4 h-4" /> Diagnostic Services</div>
                        <div className="p-2 flex-1 overflow-auto max-h-[1000px]">
                            <table className="w-full text-xs text-left border-collapse">
                                <tbody className="divide-y divide-slate-100 font-semibold text-slate-700">
                                    {data.diagnostics.map((item, idx) => (
                                        <tr key={idx} className="hover:bg-slate-50 transition">
                                            <td className="p-2">{item.name}</td>
                                            <td className="p-2 text-right font-bold text-slate-900">{item.count}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                        <div className="m-2 mt-3 bg-purple-50 border border-purple-100 rounded-lg p-3 text-center font-black text-purple-700">
                            Total Tests&nbsp;&nbsp; {totalDiagnostics}
                        </div>
                    </div>

                    {/* Consultations */}
                    <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                        <div className="bg-teal-700 px-4 py-3 text-white font-bold text-xs uppercase flex items-top gap-2 tracking-wider">
                            <Users className="w-4 h-4" /> Consultations
                        </div>

                        <div className="p-2 flex-1 overflow-auto max-h-[1000px]">
                            <table className="w-full text-xs text-left border-collapse">
                                <thead className="bg-slate-100 sticky top-0 z-10">
                                    <tr className="text-slate-600 uppercase text-[10px]">
                                        <th className="p-2 text-left">Department</th>
                                        <th className="p-2 text-right">Male</th>
                                        <th className="p-2 text-right">Female</th>
                                        <th className="p-2 text-right">Total</th>
                                    </tr>
                                </thead>

                                <tbody className="divide-y divide-slate-100 font-semibold text-slate-700">
                                    {consultationRows.map((item, idx) => (
                                        <tr key={idx} className="hover:bg-slate-50 transition">
                                            <td className="p-2 truncate max-w-[140px]">{item.name}</td>
                                            <td className="p-2 text-right text-rose-600 font-bold">{item.male}</td>
                                            <td className="p-2 text-right text-emerald-600 font-bold">{item.female}</td>
                                            <td className="p-2 text-right font-bold text-slate-900">{item.count}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                        <div className="m-2 mt-3 bg-teal-50 border border-teal-100 rounded-lg p-3 text-center font-black text-teal-700">
                            Total Consultations&nbsp;&nbsp; {totalConsultations}
                        </div>
                    </div>
                    {/* Bed Occupancy */}
                    <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                        <div className="bg-rose-600 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider"><Bed className="w-4 h-4" /> Bed Occupancy</div>
                        <div className="p-2 flex-1 overflow-auto max-h-[1000px]">
                            <table className="w-full text-xs text-left border-collapse">
                                <thead className="bg-slate-100 sticky top-0 z-10">
                                    <tr className="text-slate-600 uppercase text-[10px]">
                                        <th className="p-2 text-left">Department</th>
                                        <th className="p-2 text-right">Total</th>
                                        <th className="p-2 text-right">Occupied</th>
                                        <th className="p-2 text-right">Vacant</th>
                                        <th className="p-2 text-right">PCT</th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-slate-100 font-semibold text-slate-700">
                                    {data.beds.map((bed, idx) => (
                                        <tr key={idx} className="hover:bg-slate-50 transition">
                                            <td className="p-2 font-bold">{bed.name}</td>
                                            <td className="p-2 text-center text-amber-600">{bed.total}</td>
                                            <td className="p-2 text-center text-amber-600">{bed.occupied}</td>
                                            <td className="p-2 text-center text-emerald-600">{bed.vacant}</td>
                                            <td className="p-2 text-right font-bold text-slate-900">{bed.pct}%</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                        <div className="m-2 mt-3 bg-rose-50 border border-rose-100 rounded-lg p-3 text-center font-black text-rose-700">
                            Overall Occupancy&nbsp;&nbsp; {overallOccupancy}%
                        </div>
                    </div>
                </section>
            </div>
            {settings?.show_footer !== false && (
                <div className="marquee-container">
                    <div className="marquee-text">
                        {settings?.marquee_text || "Powered by D-Code Technology Pvt. Ltd."}
                    </div>
                </div>
            )}
        </div>
    );
}
