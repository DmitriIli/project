import React, { useState } from "react";



const Search = () => {


    return (
        <div className="search">
            <form>
                <input type="text" placeholder="Заводской номер" />
                <button>Поиск</button>
            </form>
        </div>
    );
};

export default Search