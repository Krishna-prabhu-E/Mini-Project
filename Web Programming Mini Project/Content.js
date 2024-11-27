import React from "react";

import { Itemlist } from "./Itemlist";

const Content = ({items , handleClick, handleDelete}) => {
 

  return (
    <main className="main">

    { (items.length) ?
     <Itemlist  
     items={items}
        handleClick={handleClick}
        handleDelete={handleDelete}
        /> : 
     ( <p>Your have done your work fantastically</p>)
  }
    </main>
  );
};

export default Content;
