import React from "react";

export const Search = ({ search, setSearch }) => {
  return (
    <form className="searchForm" role ="search" onSubmit={(e) => e.preventDefault()}>
      <label htmlFor="search">Search</label>
      <input
        type="text"
        id="search"
        placeholder="Search Item"
        value={search}
      
        onChange={(e) => setSearch(e.target.value)}
      />
    </form>
  );
};
