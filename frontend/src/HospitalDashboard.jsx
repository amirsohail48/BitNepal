import React from 'react';
import {
    Users, User, Shield, PieChart, BarChart3,
    Activity, ClipboardList, Bed, RefreshCw, Calendar
} from 'lucide-react';

export default function HospitalDashboard() {
    // Mock data matching the dashboard image
    const data = {
        dateFrom: "05/04/2026",
        dateTo: "05/04/2026",
        demographics: {
            female: { count: 482, percentage: 66 },
            male: { count: 252, percentage: 34 },
            total: 734,
            insuranceCoverage: { percentage: 87, count: 641 }
        },
        paymentTypes: {
            coPay: { count: 533, percentage: 72.6, female: 362, male: 171 },
            nonPay: { count: 108, percentage: 14.7, female: 60, male: 48 },
            general: { count: 92, percentage: 12.5, female: 0, male: 92 } // Adjusted breakdown for representation
        },
        diagnostics: [
            { name: "X-ray", count: 141 }, { name: "CT Scan", count: 7 },
            { name: "Ultrasonogram (USG)", count: 97 }, { name: "MRI", count: 0 },
            { name: "Echocardiogram (Echo)", count: 18 }, { name: "EEG", count: 0 },
            { name: "Electrocardiogram (ECG)", count: 49 }, { name: "Others", count: 0 },
            { name: "Laboratory Services", count: 1395 }
        ],
        consultations: [
            { name: "GENERAL MEDICINE", count: 221 }, { name: "OPHTHALMOLOGY", count: 35 },
            { name: "INTERNAL MEDICINE", count: 164 }, { name: "GENERAL SURGERY", count: 39 },
            { name: "ORTHOPEDICS", count: 117 }, { name: "DENTAL", count: 23 },
            { name: "GYNAE/OBS", count: 70 }, { name: "HOMEOPATHIC", count: 10 },
            { name: "ENT", count: 32 }, { name: "PSYCHIATRIC", count: 5 },
            { name: "PEDIATRIC", count: 28 }, { name: "Other Departments", count: 31 }
        ],
        beds: [
            { name: "Gynae", total: 7, occupied: 0, vacant: 7, pct: 0 },
            { name: "HDU", total: 5, occupied: 1, vacant: 4, pct: 20 },
            { name: "ICU", total: 5, occupied: 0, vacant: 5, pct: 0 },
            { name: "Isolation", total: 1, occupied: 0, vacant: 1, pct: 0 },
            { name: "Medicine", total: 7, occupied: 7, vacant: 0, pct: 100 },
            { name: "Ortho Surgery", total: 13, occupied: 5, vacant: 8, pct: 38 },
            { name: "Pediatric", total: 5, occupied: 3, vacant: 2, pct: 60 },
        ]
    };

    return (
        <div className="bg-slate-100 min-h-screen p-4 font-sans text-slate-800 antialiased selection:bg-blue-500 selection:text-white">
            {/* --- TOP BAR / HEADER --- */}
            <header className="bg-white rounded-xl shadow-sm p-4 mb-6 flex flex-col md:flex-row justify-between items-center gap-4">
                <div className="flex items-center gap-4">
                    <div className="w-16 h-16 bg-red-500 rounded-full flex items-center justify-center text-white font-bold text-xs text-center p-1 border-2 border-blue-900">
                        HOSPITAL LOGO
                    </div>
                    <div>
                        <h1 className="text-xl md:text-2xl font-black tracking-tight text-blue-900">MADAN BHANDARI HOSPITAL & TRAUMA CENTER</h1>
                        <p className="text-xs italic font-medium text-emerald-600">Excellence in Care, Every Time</p>
                    </div>
                </div>

                {/* Date Filter Controls */}
                <div className="flex flex-wrap items-center gap-3 text-xs">
                    <div className="flex flex-col">
                        <span className="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1">From Date</span>
                        <div className="flex items-center gap-2 border rounded-lg px-3 py-2 bg-slate-50">
                            <Calendar className="w-4 h-4 text-slate-400" />
                            <span className="font-semibold">{data.dateFrom}</span>
                        </div>
                    </div>
                    <div className="flex flex-col">
                        <span className="text-[10px] uppercase tracking-wider text-slate-400 font-bold mb-1">To Date</span>
                        <div className="flex items-center gap-2 border rounded-lg px-3 py-2 bg-slate-50">
                            <Calendar className="w-4 h-4 text-slate-400" />
                            <span className="font-semibold">{data.dateTo}</span>
                        </div>
                    </div>
                    <button className="mt-4 bg-blue-600 hover:bg-blue-700 transition text-white px-4 py-2 rounded-lg font-bold flex items-center gap-2 shadow-sm shadow-blue-200">
                        <RefreshCw className="w-3.5 h-3.5" /> Refresh
                    </button>
                </div>
            </header>

            {/* --- SECTION 1: TOP SUMMARY KPI CARDS --- */}
            <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                {/* Female Patients */}
                <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-emerald-500 flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <div className="w-12 h-12 rounded-full bg-emerald-50 flex items-center justify-center text-emerald-500">
                            <User className="w-6 h-6" />
                        </div>
                        <div>
                            <span className="text-xs uppercase font-bold text-emerald-600 tracking-wider">Female Patients</span>
                            <h2 className="text-3xl font-extrabold text-slate-900 mt-0.5">{data.demographics.female.count}</h2>
                            <p className="text-xs text-slate-400 font-medium">{data.demographics.female.percentage}% of Total Patients</p>
                        </div>
                    </div>
                    <div className="text-emerald-500 text-xs font-bold bg-emerald-50 px-2 py-1 rounded-md">📈 Spark</div>
                </div>

                {/* Male Patients */}
                <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-rose-500 flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <div className="w-12 h-12 rounded-full bg-rose-50 flex items-center justify-center text-rose-500">
                            <User className="w-6 h-6" />
                        </div>
                        <div>
                            <span className="text-xs uppercase font-bold text-rose-600 tracking-wider">Male Patients</span>
                            <h2 className="text-3xl font-extrabold text-slate-900 mt-0.5">{data.demographics.male.count}</h2>
                            <p className="text-xs text-slate-400 font-medium">{data.demographics.male.percentage}% of Total Patients</p>
                        </div>
                    </div>
                    <div className="text-rose-500 text-xs font-bold bg-rose-50 px-2 py-1 rounded-md">📈 Spark</div>
                </div>

                {/* Total Patients */}
                <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-blue-600 flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <div className="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-blue-600">
                            <Users className="w-6 h-6" />
                        </div>
                        <div>
                            <span className="text-xs uppercase font-bold text-blue-600 tracking-wider">Total Patients</span>
                            <h2 className="text-3xl font-extrabold text-slate-900 mt-0.5">{data.demographics.total}</h2>
                            <p className="text-xs text-slate-400 font-medium">100% of Total Patients</p>
                        </div>
                    </div>
                    <div className="text-blue-600 text-xs font-bold bg-blue-50 px-2 py-1 rounded-md">📈 Spark</div>
                </div>

                {/* Insurance Coverage */}
                <div className="bg-white rounded-xl p-4 shadow-sm border-l-4 border-purple-600 flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <div className="w-12 h-12 rounded-full bg-purple-50 flex items-center justify-center text-purple-600">
                            <Shield className="w-6 h-6" />
                        </div>
                        <div>
                            <span className="text-xs uppercase font-bold text-purple-600 tracking-wider">Insurance Coverage</span>
                            <h2 className="text-3xl font-extrabold text-slate-900 mt-0.5">{data.demographics.insuranceCoverage.percentage}%</h2>
                            <p className="text-xs text-slate-400 font-medium">{data.demographics.insuranceCoverage.count} of {data.demographics.total} Patients</p>
                        </div>
                    </div>
                    <div className="text-purple-600 text-xs font-bold bg-purple-50 px-2 py-1 rounded-md">📈 Spark</div>
                </div>
            </section>

            {/* --- SECTION 2: PAYMENT TYPE GRAPHICS & METRICS --- */}
            <section className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">

                {/* Card 1: Patients by Payment Type (Donut Breakdown Simulation) */}
                <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div className="bg-blue-900 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                        <PieChart className="w-4 h-4" /> Patients by Payment Type
                    </div>
                    <div className="p-6 flex flex-col items-center justify-center flex-1">
                        {/* Mocking the dynamic circular chart layout */}
                        <div className="relative w-40 h-40 rounded-full border-[16px] border-blue-600 flex flex-col items-center justify-center shadow-inner mb-6">
                            <span className="text-2xl font-black text-slate-900">{data.demographics.total}</span>
                            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-tight">Total Patients</span>
                        </div>
                        <div className="w-full space-y-2 text-xs font-semibold">
                            <div className="flex justify-between items-center text-blue-600">
                                <span>🔵 Insurance Co-Pay: {data.paymentTypes.coPay.count}</span>
                                <span>{data.paymentTypes.coPay.percentage}%</span>
                            </div>
                            <div className="flex justify-between items-center text-orange-500">
                                <span>🟠 Insurance Non-Pay: {data.paymentTypes.nonPay.count}</span>
                                <span>{data.paymentTypes.nonPay.percentage}%</span>
                            </div>
                            <div className="flex justify-between items-center text-emerald-600">
                                <span>🟢 General / Non-Bima: {data.paymentTypes.general.count}</span>
                                <span>{data.paymentTypes.general.percentage}%</span>
                            </div>
                        </div>
                    </div>
                    <div className="border-t bg-slate-50 p-3 grid grid-cols-2 text-center text-xs font-bold divide-x divide-slate-200">
                        <div className="text-blue-700">Insurance: 641 (87.3%)</div>
                        <div className="text-slate-600">Non-Insurance: 92 (12.5%)</div>
                    </div>
                </div>

                {/* Card 2: Patients by Payment Type & Gender (Stacked Bar Chart Simulation) */}
                <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div className="bg-emerald-700 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                        <BarChart3 className="w-4 h-4" /> Patients by Payment Type & Gender
                    </div>
                    <div className="p-6 flex-1 flex flex-col justify-end">
                        {/* Simple stacked column representation */}
                        <div className="grid grid-cols-3 gap-4 items-end h-48 border-b border-l pb-2 px-2 border-slate-200 text-center">
                            {/* Co-Pay Column */}
                            <div className="flex flex-col items-center h-full justify-end">
                                <span className="text-[10px] font-bold mb-1 text-slate-700">533</span>
                                <div className="w-full bg-emerald-500 h-[65%] rounded-t-sm relative group">
                                    <span className="absolute inset-0 flex items-center justify-center text-[10px] font-bold text-white">362</span>
                                </div>
                                <div className="w-full bg-rose-500 h-[30%] rounded-b-sm relative group">
                                    <span className="absolute inset-0 flex items-center justify-center text-[10px] font-bold text-white">171</span>
                                </div>
                                <span className="text-[9px] font-bold text-slate-500 mt-2 truncate max-w-full">Co-Pay</span>
                            </div>

                            {/* Non-Pay Column */}
                            <div className="flex flex-col items-center h-full justify-end">
                                <span className="text-[10px] font-bold mb-1 text-slate-700">108</span>
                                <div className="w-full bg-emerald-500 h-[20%] rounded-t-sm relative">
                                    <span className="absolute inset-0 flex items-center justify-center text-[8px] font-bold text-white">60</span>
                                </div>
                                <div className="w-full bg-rose-500 h-[15%] rounded-b-sm relative">
                                    <span className="absolute inset-0 flex items-center justify-center text-[8px] font-bold text-white">48</span>
                                </div>
                                <span className="text-[9px] font-bold text-slate-500 mt-2 truncate max-w-full">Non-Pay</span>
                            </div>

                            {/* General Column */}
                            <div className="flex flex-col items-center h-full justify-end">
                                <span className="text-[10px] font-bold mb-1 text-slate-700">92</span>
                                <div className="w-full bg-slate-400 h-[30%] rounded-t-sm relative">
                                    <span className="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-white">92</span>
                                </div>
                                <span className="text-[9px] font-bold text-slate-500 mt-2 truncate max-w-full">General</span>
                            </div>
                        </div>
                    </div>
                    <div className="border-t bg-slate-50 p-3 flex justify-center gap-6 text-xs font-bold">
                        <span className="flex items-center gap-1.5 text-emerald-600">🟢 Female: 482 (66%)</span>
                        <span className="flex items-center gap-1.5 text-rose-600">🔴 Male: 252 (34%)</span>
                    </div>
                </div>

                {/* Card 3: Patient Breakdown Totals Progress Horizontal Bars */}
                <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div className="bg-orange-600 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                        <ClipboardList className="w-4 h-4" /> Patients by Payment Type (Total)
                    </div>
                    <div className="p-6 space-y-5 flex-1 justify-center flex flex-col">
                        {/* Progress Row 1 */}
                        <div>
                            <div className="flex justify-between items-center text-xs font-bold mb-1.5">
                                <span className="text-slate-700">Insurance Co-Pay</span>
                                <span className="text-blue-700">533 <span className="text-slate-400 font-normal">(72.6%)</span></span>
                            </div>
                            <div className="w-full bg-slate-100 h-3.5 rounded-full overflow-hidden">
                                <div className="bg-blue-600 h-full rounded-full" style={{ width: '72.6%' }}></div>
                            </div>
                        </div>
                        {/* Progress Row 2 */}
                        <div>
                            <div className="flex justify-between items-center text-xs font-bold mb-1.5">
                                <span className="text-slate-700">Insurance Non-Pay</span>
                                <span className="text-orange-600">108 <span className="text-slate-400 font-normal">(14.7%)</span></span>
                            </div>
                            <div className="w-full bg-slate-100 h-3.5 rounded-full overflow-hidden">
                                <div className="bg-orange-500 h-full rounded-full" style={{ width: '14.7%' }}></div>
                            </div>
                        </div>
                        {/* Progress Row 3 */}
                        <div>
                            <div className="flex justify-between items-center text-xs font-bold mb-1.5">
                                <span className="text-slate-700">General / Non-Bima</span>
                                <span className="text-emerald-700">92 <span className="text-slate-400 font-normal">(12.5%)</span></span>
                            </div>
                            <div className="w-full bg-slate-100 h-3.5 rounded-full overflow-hidden">
                                <div className="bg-emerald-500 h-full rounded-full" style={{ width: '12.5%' }}></div>
                            </div>
                        </div>
                    </div>
                    <div className="border-t bg-amber-50 p-3 text-center text-sm font-black text-amber-900 flex items-center justify-center gap-2">
                        <Users className="w-4 h-4 text-amber-700" /> Total Patients: {data.demographics.total}
                    </div>
                </div>
            </section>

            {/* --- SECTION 3: TABULAR CORE HOSPITAL LOGISTICS --- */}
            <section className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                {/* Table 1: Diagnostic Services */}
                <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div className="bg-purple-900 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                        <Activity className="w-4 h-4" /> Diagnostic Services
                    </div>
                    <div className="p-2 flex-1 overflow-auto max-h-[340px]">
                        <table className="w-full text-xs text-left border-collapse">
                            <thead>
                                <tr className="bg-slate-50 border-b border-slate-200 text-slate-400 font-bold uppercase text-[10px]">
                                    <th className="p-2.5">Particulars</th>
                                    <th className="p-2.5 text-right">Number</th>
                                </tr>
                            </thead>
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
                    <div className="border-t bg-purple-50 p-3 text-center text-xs font-black text-purple-900">
                        Total Tests: 1,707
                    </div>
                </div>

                {/* Table 2: Consultations */}
                <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div className="bg-teal-700 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                        <Users className="w-4 h-4" /> Consultations
                    </div>
                    <div className="p-2 flex-1 overflow-auto max-h-[340px]">
                        <table className="w-full text-xs text-left border-collapse">
                            <thead>
                                <tr className="bg-slate-50 border-b border-slate-200 text-slate-400 font-bold uppercase text-[10px]">
                                    <th className="p-2.5">Particulars</th>
                                    <th className="p-2.5 text-right">Number</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-100 font-semibold text-slate-700">
                                {data.consultations.map((item, idx) => (
                                    <tr key={idx} className="hover:bg-slate-50 transition">
                                        <td className="p-2 truncate max-w-[140px]">{item.name}</td>
                                        <td className="p-2 text-right font-bold text-slate-900">{item.count}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    <div className="border-t bg-teal-50 p-3 text-center text-xs font-black text-teal-900">
                        Total Consultations: 805
                    </div>
                </div>

                {/* Table 3: Bed Occupancy */}
                <div className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col justify-between">
                    <div className="bg-rose-600 px-4 py-3 text-white font-bold text-xs uppercase flex items-center gap-2 tracking-wider">
                        <Bed className="w-4 h-4" /> Bed Occupancy
                    </div>
                    <div className="p-2 flex-1 overflow-auto max-h-[340px]">
                        <table className="w-full text-xs text-left border-collapse">
                            <thead>
                                <tr className="bg-slate-50 border-b border-slate-200 text-slate-400 font-bold uppercase text-[10px]">
                                    <th className="p-2">Particulars</th>
                                    <th className="p-2 text-center">Total</th>
                                    <th className="p-2 text-center">Occ</th>
                                    <th className="p-2 text-center">Vac</th>
                                    <th className="p-2 text-right">Occ %</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-100 font-semibold text-slate-700">
                                {data.beds.map((bed, idx) => (
                                    <tr key={idx} className="hover:bg-slate-50 transition">
                                        <td className="p-2 font-bold">{bed.name}</td>
                                        <td className="p-2 text-center">{bed.total}</td>
                                        <td className="p-2 text-center text-amber-600">{bed.occupied}</td>
                                        <td className="p-2 text-center text-emerald-600">{bed.vacant}</td>
                                        <td className="p-2 text-right font-bold text-slate-900">{bed.pct}%</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    <div className="border-t bg-rose-50 p-3 flex justify-between items-center text-xs font-black text-rose-900 px-4">
                        <span>Overall Occupancy</span>
                        <span className="text-sm font-extrabold text-rose-700">32%</span>
                    </div>
                </div>

            </section>
        </div>
    );
}