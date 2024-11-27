import "./App.css";
import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";
import { useState, useRef } from "react";
import Additem from "./Additem";
import { Search } from "./Search";
function App() {
  const [newItem, setNewitem] = useState("");
  const inputRef = useRef();

  function handleNewitem(item) {}
  function handleSubmit(e) {
    e.preventDefault();
    console.log(newItem);
    addItem(newItem);
    setNewitem("");
    console.log("Submitted");
  }

  const [items, setItems] = useState(
    JSON.parse(localStorage.getItem("to_do_list")) || []
  );
  const handleClick = (id) => {
    const listItems = items.map((item) =>
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setItems(listItems);
    localStorage.setItem("to_do_list", JSON.stringify(listItems));
  };
  const addItem = (item) => {
    const id = items.length ? items[items.length - 1].id + 1 : 1;
    const newItems = { id: id, checked: false, item: item };

    const listItems = [...items, newItems];

    setItems(listItems);
    localStorage.setItem("to_do_list", JSON.stringify(listItems));
    console.log(listItems);
  };

  const handleDelete = (id) => {
    const listItems = items.filter((item) => item.id !== id);
    setItems(listItems);
    localStorage.setItem("to_do_list", JSON.stringify(listItems));
  };

  const [search, setSearch] = useState("");
  return (
    <div className="App">
      <Header title="To do List " />
      <Additem
        newItem={newItem}
        setNewitem={setNewitem}
        handleNewitem={handleNewitem}
        handleSubmit={handleSubmit}
        inputRef={inputRef}
      />
      <Search search={search} setSearch={setSearch} />
      <Content
        items={items.filter((item) =>
          item.item.toLowerCase().includes(search.toLowerCase())
        )}
        handleClick={handleClick}
        handleDelete={handleDelete}
      />
      <Footer length={items.length} />
    </div>
  );
}

export default App;
