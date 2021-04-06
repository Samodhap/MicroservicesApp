import React, {useEffect,useState} from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [products, setProducts] = useState(null);

    const fetchData = async () => {
        const response = await axios.get(
            'http://localhost:8080/product-catalog/products/'
        );

        setProducts(response.data);
    };

    // useEffect(() => {
    //
    //     fetchData()
    // })

    return (
        <div className="App">
            <h1>Product Catalog</h1>

            {/* Fetch data from API */}
            <div>
                <button className="fetch-button" onClick={fetchData}>
                    Fetch Product Data
                </button>
                <br/>
            </div>

            {/* Display data from API */}
            <div className="products">
                {products &&
                products.map(product => {
                    return (
                        <div className="product" key={product.product_name}>
                            <h3>{product.product_name}</h3>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}

export default App;
