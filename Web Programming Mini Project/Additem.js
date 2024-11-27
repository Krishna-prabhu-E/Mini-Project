import React from "react";
import { FaPlus } from "react-icons/fa";

const Additem = ({newItem , setNewitem  ,  inputRef,handleSubmit}) => {
  return (
    <form className="addForm" onSubmit={handleSubmit}>
      <label htmlFor="addItem"> </label>
        <input
          type="text"
          placeholder="Enter an Item"
          required
          ref = {inputRef}
          autoFocus
          id="addItem"
          value={newItem}
          onChange={(e) =>  setNewitem(e.target.value)}
        />
        <button>
          
          <FaPlus onClick={() => inputRef.current.focus()}/>
        </button>
     
    </form>
  );
};

export default Additem;
