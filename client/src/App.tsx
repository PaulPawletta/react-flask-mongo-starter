import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import "./App.css";
import ButtonAppBar from "./components/ButtonAppBar";
import DocumentsPage from "./pages/DocumentsPage";
import RulesPage from "./pages/RulesPage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <ButtonAppBar />
        <Route exact path="/documents">
          <DocumentsPage />
        </Route>
        <Route exact path="/rules">
          <RulesPage />
        </Route>
      </BrowserRouter>
    </div>
  );
}

export default App;
