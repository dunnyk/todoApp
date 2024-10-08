import React, { useState, useEffect } from "react";

const TaskDisplay = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);

  // Fetch tasks from the API only if the user is logged in
  useEffect(() => {
    const fetchTasks = async () => {
      const token = localStorage.getItem("token");
      // If there's no token, the user is not logged in
      if (!token) {
        setError("User is not logged in. Please log in to view tasks.");
        return;
      }

      try {
        const response = await fetch(
          "http://localhost:5002/tasks/task_create",
          {
            method: "GET",
            headers: {
              Authorization: `Bearer ${token}`, // Include the token in the request headers
              "Content-Type": "application/json",
            },
          }
        );

        if (!response.ok) {
          if (response.status === 401) {
            throw new Error("Unauthorized. Please log in again.");
          } else {
            throw new Error("Failed to fetch tasks.");
          }
        }

        const data = await response.json();
        setTasks(data.tasks_dict);
      } catch (error) {
        setError(error.message);
      }
    };

    fetchTasks();
  }, []);

  return (
    <div className="task-container">
      <h2>Tasks</h2>
      {error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : (
        <ul>
          {tasks.length > 0 ? (
            tasks.map((task) => (
              <li key={task.id}>
                <strong>{task.task_name}</strong>: {task.description}
              </li>
            ))
          ) : (
            <p>No tasks available</p>
          )}
        </ul>
      )}
    </div>
  );
};

export default TaskDisplay;
