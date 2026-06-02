import React, { useEffect, useState } from "react";
import { Building2, Image, LogIn, LogOut, Save, Upload } from "lucide-react";

function getCookie(name) {
    const cookies = document.cookie ? document.cookie.split("; ") : [];

    for (const cookie of cookies) {
        const parts = cookie.split("=");
        const key = decodeURIComponent(parts[0]);

        if (key === name) {
            return decodeURIComponent(parts.slice(1).join("="));
        }
    }

    return "";
}

export default function AdminSettings() {
    const [auth, setAuth] = useState({
        authenticated: false,
        username: "",
        is_staff: false,
    });

    const [loginForm, setLoginForm] = useState({
        username: "",
        password: "",
    });

    const [settings, setSettings] = useState({
        hospital_name: "",
        company_name: "",
        theme_color: "blue",
        auto_refresh_seconds: 30,
        marquee_text: "",
        show_footer: true,
        hospital_logo: "",
        company_logo: "",
    });

    const [hospitalLogoFile, setHospitalLogoFile] = useState(null);
    const [companyLogoFile, setCompanyLogoFile] = useState(null);

    const [hospitalLogoPreview, setHospitalLogoPreview] = useState("");
    const [companyLogoPreview, setCompanyLogoPreview] = useState("");

    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);

    const prepareCsrf = async () => {
        await fetch("/dash/csrf/", {
            credentials: "include",
        });
    };

    const fetchAuthStatus = async () => {
        const response = await fetch("/dash/auth/status/", {
            credentials: "include",
        });

        const data = await response.json();
        setAuth(data);
    };

    const fetchSettings = async () => {
        const response = await fetch("/dash/settings/", {
            credentials: "include",
        });

        const data = await response.json();

        setSettings({
            hospital_name: data.hospital_name || "",
            company_name: data.company_name || "",
            theme_color: data.theme_color || "blue",
            auto_refresh_seconds: data.auto_refresh_seconds || 30,
            marquee_text: data.marquee_text || "",
            show_footer: data.show_footer ?? true,
            hospital_logo: data.hospital_logo || "",
            company_logo: data.company_logo || "",
        });

        setHospitalLogoPreview(data.hospital_logo || "");
        setCompanyLogoPreview(data.company_logo || "");
    };

    useEffect(() => {
        prepareCsrf();
        fetchAuthStatus();
        fetchSettings();
    }, []);

    const handleLogin = async (e) => {
        e.preventDefault();

        setLoading(true);
        setMessage("");

        try {
            await prepareCsrf();

            const response = await fetch("/dash/auth/login/", {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify(loginForm),
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Login failed");
            }

            setMessage("Login successful.");
            await fetchAuthStatus();
        } catch (error) {
            setMessage(error.message || "Login failed");
        } finally {
            setLoading(false);
        }
    };

    const handleLogout = async () => {
        setLoading(true);
        setMessage("");

        try {
            await fetch("/dash/auth/logout/", {
                method: "POST",
                credentials: "include",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            });

            setAuth({
                authenticated: false,
                username: "",
                is_staff: false,
            });

            setMessage("Logged out successfully.");
        } catch (error) {
            setMessage("Logout failed.");
        } finally {
            setLoading(false);
        }
    };

    const handleHospitalLogoChange = (e) => {
        const file = e.target.files[0];

        if (file) {
            setHospitalLogoFile(file);
            setHospitalLogoPreview(URL.createObjectURL(file));
        }
    };

    const handleCompanyLogoChange = (e) => {
        const file = e.target.files[0];

        if (file) {
            setCompanyLogoFile(file);
            setCompanyLogoPreview(URL.createObjectURL(file));
        }
    };

    const handleSave = async (e) => {
        e.preventDefault();

        setLoading(true);
        setMessage("");

        const formData = new FormData();

        formData.append("hospital_name", settings.hospital_name);
        formData.append("company_name", settings.company_name);
        formData.append("theme_color", settings.theme_color);
        formData.append("auto_refresh_seconds", settings.auto_refresh_seconds);
        formData.append("marquee_text", settings.marquee_text);
        formData.append("show_footer", settings.show_footer ? "true" : "false");

        if (hospitalLogoFile) {
            formData.append("hospital_logo", hospitalLogoFile);
        }

        if (companyLogoFile) {
            formData.append("company_logo", companyLogoFile);
        }

        try {
            await prepareCsrf();

            const response = await fetch("/dash/settings/", {
                method: "POST",
                credentials: "include",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Failed to save settings");
            }

            setMessage("Settings saved successfully.");
            await fetchSettings();
        } catch (error) {
            setMessage(error.message || "Save failed.");
        } finally {
            setLoading(false);
        }
    };

    if (!auth.authenticated || !auth.is_staff) {
        return (
            <div className="min-h-screen bg-slate-100 flex items-center justify-center p-6">
                <div className="w-full max-w-md bg-white rounded-2xl shadow-sm border overflow-hidden">
                    <div className="bg-blue-500 text-white px-6 py-4">
                        <h1 className="text-xl font-black flex items-center gap-2">
                            <LogIn className="w-5 h-5" />
                            Dashboard Admin Login
                        </h1>
                        <p className="text-xs text-blue-100 mt-1">
                            Login is required to update dashboard settings.
                        </p>
                    </div>

                    <form onSubmit={handleLogin} className="p-6 space-y-4">
                        <div>
                            <label className="block text-xs font-bold text-slate-500 uppercase mb-1">
                                Username
                            </label>
                            <input
                                type="text"
                                value={loginForm.username}
                                onChange={(e) =>
                                    setLoginForm({ ...loginForm, username: e.target.value })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold"
                                required
                            />
                        </div>

                        <div>
                            <label className="block text-xs font-bold text-slate-500 uppercase mb-1">
                                Password
                            </label>
                            <input
                                type="password"
                                value={loginForm.password}
                                onChange={(e) =>
                                    setLoginForm({ ...loginForm, password: e.target.value })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold"
                                required
                            />
                        </div>

                        {message && (
                            <div className="bg-slate-100 border rounded-lg px-4 py-3 text-sm font-semibold text-slate-700">
                                {message}
                            </div>
                        )}

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full bg-blue-900 hover:bg-blue-950 disabled:bg-slate-400 text-white px-6 py-3 rounded-xl font-black flex items-center justify-center gap-2"
                        >
                            <LogIn className="w-4 h-4" />
                            {loading ? "Please wait..." : "Login"}
                        </button>
                    </form>
                </div>
            </div>
        );
    }

    return (
        <div className="w-full min-h-screen bg-slate-100 p-6 font-sans">
            <div className="max-w-5xl mx-auto bg-white rounded-2xl shadow-sm border overflow-hidden">
                <div className="bg-blue-400 px-6 py-4 text-white flex justify-between items-center">
                    <div>
                        <h1 className="text-xl font-black flex items-center gap-2">
                            <Building2 className="w-5 h-5" />
                            Dashboard Admin Settings
                        </h1>
                        <p className="text-xs text-blue-100 mt-1">
                            Logged in as {auth.username}
                        </p>
                    </div>

                    <button
                        onClick={handleLogout}
                        className="bg-white text-blue-900 px-4 py-2 rounded-lg font-bold text-xs flex items-center gap-2"
                    >
                        <LogOut className="w-4 h-4" />
                        Logout
                    </button>
                </div>

                <form onSubmit={handleSave} className="p-6 space-y-6">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                        <div>
                            <label className="block text-xs font-bold uppercase text-slate-500 mb-1">
                                Hospital Name
                            </label>
                            <input
                                type="text"
                                value={settings.hospital_name}
                                onChange={(e) =>
                                    setSettings({ ...settings, hospital_name: e.target.value })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold"
                            />
                        </div>

                        <div>
                            <label className="block text-xs font-bold uppercase text-slate-500 mb-1">
                                Company Name
                            </label>
                            <input
                                type="text"
                                value={settings.company_name}
                                onChange={(e) =>
                                    setSettings({ ...settings, company_name: e.target.value })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold"
                            />
                        </div>

                        <div>
                            <label className="block text-xs font-bold uppercase text-slate-500 mb-1">
                                Theme Color
                            </label>
                            <select
                                value={settings.theme_color}
                                onChange={(e) =>
                                    setSettings({ ...settings, theme_color: e.target.value })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold bg-white"
                            >
                                <option value="blue">Blue</option>
                                <option value="green">Green</option>
                                <option value="purple">Purple</option>
                                <option value="red">Red</option>
                            </select>
                        </div>

                        <div>
                            <label className="block text-xs font-bold uppercase text-slate-500 mb-1">
                                Auto Refresh Seconds
                            </label>
                            <input
                                type="number"
                                value={settings.auto_refresh_seconds}
                                onChange={(e) =>
                                    setSettings({
                                        ...settings,
                                        auto_refresh_seconds: Number(e.target.value),
                                    })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold"
                            />
                        </div>

                        <div className="md:col-span-2">
                            <label className="block text-xs font-bold uppercase text-slate-500 mb-1">
                                Marquee Text
                            </label>
                            <input
                                type="text"
                                value={settings.marquee_text}
                                onChange={(e) =>
                                    setSettings({ ...settings, marquee_text: e.target.value })
                                }
                                className="w-full border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500 font-semibold"
                            />
                        </div>

                        <div className="md:col-span-2 flex items-center gap-3">
                            <input
                                type="checkbox"
                                checked={settings.show_footer}
                                onChange={(e) =>
                                    setSettings({ ...settings, show_footer: e.target.checked })
                                }
                            />
                            <span className="text-sm font-bold text-slate-700">
                                Show footer / marquee
                            </span>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <LogoUploadBox
                            title="Hospital Logo"
                            preview={hospitalLogoPreview}
                            onChange={handleHospitalLogoChange}
                        />

                        <LogoUploadBox
                            title="Company Logo"
                            preview={companyLogoPreview}
                            onChange={handleCompanyLogoChange}
                        />
                    </div>

                    {message && (
                        <div className="bg-slate-100 border rounded-lg px-4 py-3 text-sm font-semibold text-slate-700">
                            {message}
                        </div>
                    )}

                    <button
                        type="submit"
                        disabled={loading}
                        className="bg-blue-400 hover:bg-blue-600 disabled:bg-slate-400 text-white px-6 py-3 rounded-xl font-black flex items-center gap-2"
                    >
                        <Save className="w-4 h-4" />
                        {loading ? "Saving..." : "Save Settings"}
                    </button>
                </form>
            </div>
        </div>
    );
}

function LogoUploadBox({ title, preview, onChange }) {
    return (
        <div className="border rounded-xl p-4 bg-slate-50">
            <label className="block text-xs font-bold uppercase text-slate-500 mb-3">
                {title}
            </label>

            <div className="h-40 bg-white border rounded-xl flex items-center justify-center overflow-hidden mb-4">
                {preview ? (
                    <img
                        src={preview}
                        alt={title}
                        className="max-h-36 max-w-full object-contain"
                    />
                ) : (
                    <Image className="w-12 h-12 text-slate-300" />
                )}
            </div>

            <label className="cursor-pointer bg-blue-400 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-bold text-xs flex items-center justify-center gap-2">
                <Upload className="w-4 h-4" />
                Upload
                <input
                    type="file"
                    accept="image/*"
                    onChange={onChange}
                    className="hidden"
                />
            </label>
        </div>
    );
}