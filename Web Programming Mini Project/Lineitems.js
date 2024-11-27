import React from 'react'
import { FaTrash } from "react-icons/fa";
const Lineitems = ({item , handleClick , handleDelete}) => {
  return (
    <li className="item" > 
          <input
            type="checkbox"
            checked={item.checked}
            onChange={() => handleClick(item.id)}
          />

          <label
            onDoubleClick={() => handleClick(item.id)}
            style={item.checked ? { textDecoration: "line-through" } : null}
          >
            {item.item}
          </label>
          <FaTrash
            role="button"
            tabIndex="0"
            onClick={() => handleDelete(item.id)}
          />
        </li>
  )
}

export default Lineitems