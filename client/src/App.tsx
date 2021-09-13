import React from "react";
import "./App.css";
import ButtonAppBar from "./components/ButtonAppBar";
import axios from "axios";

interface ITodo {
  title: string;
  content: string;
}

function App() {
  const defaultTodos: ITodo[] = [];
  const [todos, setTodos]: [ITodo[], (todos: ITodo[]) => void] =
    React.useState(defaultTodos);

  React.useEffect(() => {
    axios
      .get("http://localhost:5000/api/v1/todos/")
      .then((response) => {
        // setTodos(response.data);
        console.log(response)
      });
  }, []);

  return (
    <div className="App">
      <ButtonAppBar />
      <ul className="todos">
        {todos.map((todo) => (
          <li>
            <h3>{todo.title}</h3>
            <p>{todo.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
