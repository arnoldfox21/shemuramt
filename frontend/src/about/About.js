import React, { Component } from "react";
 
class About extends React.Component {
  render() {
    return (
         <div id="main">
            <div className="wrapper">
              <section id="content">
                <div className="container">
                  <div className="section">
                         <div className="card hoverable small full_height">
                            <div className="card-image">
                              <img src="assets/images/slide1.jpg"/>
                              <span className="card-title">Hallo l</span>
                            </div>
                            <div className="card-content">
                            <span className="card-title grey-text text-darken-4">Hallo</span>
                              <p>lorem lorem lorem lorem lorem lorem </p>                    
                              <p><i className="mdi-action-perm-identity cyan-text text-darken-2"></i> Gita kumalasari</p>
                              <p><i className="mdi-communication-business cyan-text text-darken-2"></i> Kec. Lawang Kab Malang</p>
                              <p><i className="mdi-action-perm-phone-msg cyan-text text-darken-2"></i> +1 (612) 222 8989</p>
                              <p><i className="mdi-communication-email cyan-text text-darken-2"></i> help@shemura-mt.com</p>  
                            </div>
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