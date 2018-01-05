import React, { Component } from "react";
import axios from 'axios'
import LoaderPage from '../assets/LoaderComponent'
import Alert from '../assets/Alert'

class Login extends React.Component {
  constructor(props){
    super(props)
    
    this.state = {
      email: null,
      pass : null,
      isLoading: true,
      notification: [],
      loginOperations: []
    }

  }

  handleLogin(e) {
    e.preventDefault();

    var qs = require('qs');
    axios.post('http://127.0.0.1:8000/loginrequest/', qs.stringify({
      mail: this.state.email,
      pass: this.state.pass
    }))
    .then((response) => {// iki kalo status 200/ selain 200 gk masuk sini
      this.setState({notification: <Alert status={response} /> })
    })
    .catch(function (error) {
    this.setState({notification: <Alert status={error} /> })
  });
  }

  componentDidMount() {
    setTimeout(function() { 
    this.setState({isLoading: false}) 
    }.bind(this), 2000);
  }

  render() {
  if(this.state.isLoading) {
    return(<LoaderPage/>)
  } else {
    return (
             <div>
                <div className="parallax-container">
                  <div className="parallax">
                    <img src="assets/images/slide5.jpg"/>
                  </div>
                </div>
                <div className="col s12 m12 l12">
                    <center>
                     <div className="col s12 m6 l6 card-panel">
                      <div className="right top medium-small">
                         <a href="">Butuh bantuan?</a>
                      </div>
                        <div className="row">
                          <div className="input-field col l12 center">
                            <p className="center login-form-text">SHEMURA LOGIN</p>
                          </div>
                        </div>
                    {this.state.notification}
                    <form className="login-form" action={(e)=>this.handleLogin(e)} method="POST">
                        <div className="row margin">
                          <div className="input-field col s12 m12 l12">
                            <i className="mdi-social-person-outline prefix"></i>
                            <input type="hidden" name="from_url" value=""/>
                            <input 
                              id="username" 
                              name="umail" 
                              type="text"
                              onChange={(e)=>this.setState({email: e.target.value}) }/>
                            <label for="username" className="center-align">Email</label>
                          </div>
                        </div>
                        <div className="row margin">
                          <div className="input-field col s12 m12 l12">
                            <i className="mdi-action-lock-outline prefix"></i>
                            <input 
                              id="password" 
                              name="pswd" 
                              type="password"
                              onChange={(e)=>this.setState({pass: e.target.value})}/>
                            <label for="password">Password</label>
                          </div>
                        </div>
                        
                         <div className="row">          
                          <div className="input-field col s12 m12 l12  login-text">
                            <div className="g-recaptcha" data-sitekey="6Lfbly8UAAAAAOMIGVEqPYd1Os9GYD3WA2RbQhUB"></div>
                          </div>
                         </div>

                         <div className="row">          
                          <div className="input-field col s12 m12 l12  login-text">
                              
                          </div>
                        </div>
                        <div className="row">
                          <div className="input-field col s12">
                            <i className="btn purple waves-effect waves-light col s12 waves-input-wrapper">
                                <input className="waves-button-input" onClick={(e)=>this.handleLogin(e)} name="login" value="Masuk" type="submit"/>
                            </i>
                          </div>
                        </div>
                        
                     </form>
                  </div>
                </center>
                </div>
                <div className="parallax-container">
                  <div className="parallax">
                    <img src="assets/images/slide5.jpg"/>
                  </div>
                </div>
               
            </div>
              
    );
  }
  }
}
 
export default Login
