import React from "react";
import HospitalDashboard from "./HospitalDashboard";
import AdminSettings from "./AdminSettings";

export default function App() {
  const path = window.location.pathname;

  if (path === "/admin-settings" || path === "/admin-settings/") {
    return <AdminSettings />;
  }

  return <HospitalDashboard />;
}