import React, { Component } from "react";
 
class Login extends React.Component {
  constructor(props){
    super(props)
    
    this.state = {
      email: null,
      pass : null,
      loginOperations: []
    }

  }

  handleLogin(e) {
    e.preventDefault();
    console.log(this.state.email)
    console.log(this.state.pass)
    localStorage.setItem("email", this.state.email);
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/alldistributor/?format=json")
    .then(result => {
      
    })
  }

  render() {
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
                    <form className="login-form" method="POST">
                        <div className="row margin">
                          <div className="input-field col s12 m12 l12">
                            <i className="mdi-social-person-outline prefix"></i>
                            <input type="hidden" name="from_url" value=""/>
                            <input 
                              id="username" 
                              placeholder="demo: demo@shemura.com" 
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
                              placeholder="demo: demo" 
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
                              <input id="remember-me" type="checkbox"/>
                              <label for="remember-me">Ingat saya</label>
                          </div>
                        </div>
                        <div className="row">
                          <div className="input-field col s12">
                            <i className="btn purple waves-effect waves-light col s12 waves-input-wrapper">
                                <input className="waves-button-input" onClick={(e)=>this.handleLogin(e)} name="login" value="Masuk" type="submit"/>
                            </i>
                          </div>
                        </div>
                        <div className="row">
                          <div className="input-field col s12">
                            <b className="grey-text">atau masuk melalui akun google</b>
                            <br/><br/>
                             <a href="">
                                 <img className="z-depth-1 waves-light waves-effect g_login" src="assets/images/g.png"/>
                             </a>
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
                 <script src='https://www.google.com/recaptcha/api.js'></script>
            </div>
              
    );
  }
}
 
export default Login