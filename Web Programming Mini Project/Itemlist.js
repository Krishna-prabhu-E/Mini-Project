import React from "react";

import Lineitems from "./Lineitems";

export const Itemlist = ({ items, handleClick, handleDelete }) => {
  return (
    <ul>
      {items.map((item) => (
        <Lineitems 
        item  = {item}
        key = {item.id}
        handleClick = {handleClick}
        handleDelete={handleDelete}
        />
      ))}
    </ul>
  );
};
