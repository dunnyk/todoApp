// HomePage.js
import React from "react";
import { Box, Typography } from "@mui/material";
import NavBar from "../Components/NavBar";
import TaskDisplay from "../Components/Layouts/TaskDisplay";

const HomePage = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        height: "100vh",
        width: "100%",
        padding: "20px",
        paddingLeft: "0px",
      }}
    >
      <NavBar />
      <Typography variant="h3" component="h1" gutterBottom>
        Welcome to the Todo App
      </Typography>
      <Typography variant="body1" gutterBottom>
        Keep track of all your tasks easily.
      </Typography>
      <TaskDisplay />
    </Box>
  );
};

export default HomePage;
