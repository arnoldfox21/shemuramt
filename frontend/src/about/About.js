import React, { Component } from "react";
import CompanyprofileComponent from './CompanyprofileComponent'
import axios from 'axios'
 
class About extends React.Component {

  constructor(){
    super();
    this.state = {
      title: [],
      article: [],
      title_post: []
    }
  }

  componentDidMount(){
  
    axios.get('http://127.0.0.1:8000/getcompanyprofile/1/')
    .then((response) => {
      console.log(response)
      this.setState({title_post: response.data.title})
      this.setState({article: <CompanyprofileComponent idc={response.data} />});
    })
    .catch(function (error) {
    this.setState({article: <CompanyprofileComponent idc={error} />})
    });
    
  }

  render() {
    return (
         <div id="main">
            <div className="wrapper">
              <section id="content">
                <div className="container">
                  <div className="section">
                         <div className="card full_height">
                            <div className="card-image">
                              <img src="assets/images/slide1.jpg"/>
                              <span className="card-title">{this.state.title_post}</span>
                            </div>
                           {this.state.article}
                            <div className="row">
                              <div className="col s12 m6 l6">
                                  <div className="center promo promo-example">
                                      <p className="flow-text">Menerima pembayaran credit card</p>
                                     <img src="assets/images/credit-card-icons.png"/>
                                  </div>
                              </div>
                              <div className="col s12 m6 l6">
                                  <div className="center promo promo-example">
                                      <p className="flow-text">Menerima pembayaran Bank transfer</p>
                                      <img src="assets/images/rekening-baru.jpg" />
                                  </div>
                              </div>
                            </div>

                          </div>

                            <p className="caption">Punya pertanyaan jangan ragu untuk menghubungi kami, silahkan 
                            <a href="">klik disini</a> customer service kami dengan senang hati membantu anda?
                            </p>
                          <div className="divider"></div> 
                        </div>
                    </div>            
                 
              </section>
            </div>
          </div>

    );
  }
}
 
export default About
