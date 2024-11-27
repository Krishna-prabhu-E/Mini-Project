import React from "react";

const Header = (props) => {
  const { title = "default props" } = props;

  return (
    <header className="header">
      <h1>{title}</h1>
    </header>
  );
};

export default Header;
