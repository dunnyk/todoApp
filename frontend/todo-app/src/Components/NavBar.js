// NavBar.js
import React from "react";
import { AppBar, Toolbar, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import { Box } from "@mui/material";

const NavBar = () => {
  return (
    <AppBar
      position="sticky"
      bgcolour="green"
      sx={{ top: 0, bgcolor: "#76ff03", width: "90%", mx: "auto" }}
    >
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Todo App
        </Typography>
        <Box sx={{ display: "flex", gap: 2 }}>
          <Link to="/" style={{ textDecoration: "none", color: "white" }}>
            Home
          </Link>

          <Link to="/login" style={{ textDecoration: "none", color: "white" }}>
            Login
          </Link>

          <Link to="/signup" style={{ textDecoration: "none", color: "white" }}>
            Signup
          </Link>

          <Link
            to="/dashboard"
            style={{ textDecoration: "none", color: "white" }}
          >
            Dashboard
          </Link>

          <Link
            to="/profile"
            style={{ textDecoration: "none", color: "white" }}
          >
            Profile
          </Link>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
