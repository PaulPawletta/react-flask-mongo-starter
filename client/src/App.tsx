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
  const [newTodo, setNewTodo]: [ITodo, (todo: ITodo) => void] = React.useState({title: '', content: ''});

  React.useEffect(() => {
    axios.get("http://localhost:5000/api/v1/todos/").then((response) => {
      console.log(response);
      setTodos(response.data);
    });
  }, []);

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    setNewTodo({ title: event.target.value, content: event.target.value });
    console.log(newTodo);
  }

  function handleSubmit(event: any) {
    axios.post('http://localhost:5000/api/v1/todos/', newTodo)
      .then(res => {
        console.log(res);
        console.log(res.data);
      }).catch((error) => {
        console.log(error);
      })
  }

  return (
    <div className="App">
      <ButtonAppBar />
      <br/>
      <form onSubmit={handleSubmit}>
        <label>
          Title + Content:
          <input type="text" name="title" onChange={handleChange} />
        </label>
        <button type="submit">Add</button>
      </form>
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
