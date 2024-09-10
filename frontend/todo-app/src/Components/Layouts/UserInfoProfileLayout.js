import React, { useEffect, useState } from "react";
import { Card, CardContent, Typography, Avatar } from "@mui/material";

const UserInfoProfileLayout = () => {
  const [user, setUser] = useState(null);
  const [username] = useState("");
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch user info using the login endpoint
    const fetchUser = async (e) => {
      //      e.preventDefault();

      const token = localStorage.getItem("token");
      if (!token) {
        setError("No authorization token");
      }

      const userData = {
        username,
      };

      try {
        const response = await fetch("http://localhost:5002/login", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(userData),
        }); // Fetch user details from login endpoint
        if (response.ok) {
          const data = await response.json();
          console.log(">>>>>>>>>>", data);
          setUser(data); // Set user data if logged in
        } else {
          console.error("User not logged in or failed to fetch user data");
        }
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    };

    fetchUser();
  }, [username]);

  return (
    <div>
      {user ? (
        <Card sx={{ maxWidth: 300, margin: "auto", mt: 2 }}>
          <CardContent>
            <Avatar sx={{ width: 56, height: 56, margin: "auto" }}>
              {user.name.charAt(0)}
            </Avatar>
            <Typography variant="h6" align="center" mt={2}>
              {user.name}
            </Typography>
            <Typography variant="body2" color="textSecondary" align="center">
              {user.email}
            </Typography>
          </CardContent>
        </Card>
      ) : (
        <Typography variant="body1" align="center" mt={2}>
          Please log in to see user details.
        </Typography>
      )}
    </div>
  );
};

export default UserInfoProfileLayout;
