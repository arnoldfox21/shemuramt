
import React, { Component } from "react";
import {
  Route,
  HashRouter
} from "react-router-dom";
import Home from "./ListDom/Home";
import DetailProduct from "./ListDom/DetailProduct";
import Login from "./ListDom/Login";
import About from "./about/About";
import Contact from "./single_product/Contact";
import LoaderPage from "./assets/LoaderComponent"
import { sessionService } from 'redux-react-session';
 
class Main extends Component {
  render() {
    return (
      <HashRouter>
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path="/detail" component={DetailProduct}/>
            <Route path="/contact" component={Contact}/>
            <Route path="/login" component={Login}/>
            <Route path="/about" component={About}/>
            <Route path="/loader" component={LoaderPage}/>
          </div>
      </HashRouter>
    );
  }
}
 
export default Main;