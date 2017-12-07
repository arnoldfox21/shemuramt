
import React, { Component } from "react";
import {
  Route,
  HashRouter
} from "react-router-dom";
import Home from "./home/Home";
import Cart from "./cart/Cart";
import Login from "./login/Login";
import About from "./about/About";
import Contact from "./single_product/Contact";
 
class Main extends Component {
  render() {
    return (
      <HashRouter>
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/cart" component={Cart}/>
            <Route path="/contact" component={Contact}/>
            <Route path="/login" component={Login}/>
            <Route path="/about" component={About}/>
          </div>
      </HashRouter>
    );
  }
}
 
export default Main;