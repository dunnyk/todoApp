import React, { useState } from "react";
import {
  Box,
  Button,
  Container,
  TextField,
  Paper,
  Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";

const SignupForm = () => {
  const navigate = useNavigate();

  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password_hash, setPassword] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();

    const formData = {
      first_name,
      last_name,
      username,
      email,
      password_hash,
    };

    const signupResult = await fetch("http://127.0.0.1:5002/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });
    const signupInJson = await signupResult.json();
    if (!signupInJson) {
      console.log("Register 1st to log-in");
    } else {
      console.log(signupInJson);
      navigate("/login");
    }
  };

  return (
    <Container maxWidth="sm">
      <Paper elevation={3} sx={{ padding: "30px", mt: 8 }}>
        <Typography variant="h4" align="center" gutterBottom>
          Signup
        </Typography>
        <Box
          component="form"
          sx={{ display: "flex", flexDirection: "column", gap: "20px" }}
          onSubmit={handleSignup}
        >
          <TextField
            label="Firstname"
            fullWidth
            required
            value={first_name}
            onChange={(e) => setFirstName(e.target.value)}
          />

          <TextField
            label="Lastname"
            fullWidth
            required
            value={last_name}
            onChange={(e) => setLastName(e.target.value)}
          />

          <TextField
            label="Username"
            fullWidth
            required
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <TextField
            label="Email"
            type="email"
            fullWidth
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <TextField
            label="Password"
            type="password"
            fullWidth
            required
            value={password_hash}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button
            variant="contained"
            type="submit"
            color="primary"
            sx={{ marginTop: "20px" }}
          >
            Signup
          </Button>
        </Box>
      </Paper>
    </Container>
  );
};

export default SignupForm;
