import React, { Component } from "react";

 
class Home extends React.Component {
  render() {
    return (
    <div>             
        <div className="slider" slider >
            <ul className="slides">
                <li>
                    <img src="http://lorempixel.com/580/250/nature/1"/> 
                    <div className="caption center-align">
                        <h3>Selamat datang di situs resmi</h3>
                        <h5 className="light grey-text text-lighten-3">Shemura Mikasa Tani</h5>
                    </div>
                </li>
                <li>
                    <img src="http://lorempixel.com/580/250/nature/2"/> 
                    <div className="caption left-align">
                        <h3>Pabrik pupuk cair</h3>
                        <h5 className="light grey-text text-lighten-3">Solusi cerdas untuk petani.</h5>
                    </div>
                </li>
                <li>
                        <img src="http://lorempixel.com/580/250/nature/3"/> 
                        <div className="caption right-align">
                    <h3>Lebih efisien</h3>
                    <h5 className="light grey-text text-lighten-3">mudah dan tidak terlalu menguras tenaga.</h5>
                    </div>
                </li>
                <li>
                    <img src="http://lorempixel.com/580/250/nature/4"/> 
                    <div className="caption center-align">
                        <h3>This is our big Tagline!</h3>
                        <h5 className="light grey-text text-lighten-3">Here's our small slogan.</h5>
                    </div>
                </li>
            </ul>
        </div>
        <div className="col s12 banner z-depth-1 purple" id="banner_home">
            <br/>
              <h1 className="header col s12 white-text center centralize"> Selamat datang di Situs resmi kami</h1>
        <div className="green">
            <div className="row">
                  <h3 className="header col s12 white-text centralize center-align hide-on-small-only" itemprop="description">Situs ini dibangun untuk mempermudah transaksi dan melayani semua distributor Shemura MT.</h3>
              </div>
                  <div className="col s12 m8 centralize">
                    <div className="row">
                      <div className="col m12 s12"> 
                        <div className="center-align">
                            <a href="" className="waves-effect waves-light btn-large darken-1 btn-trial purple"> Masuk sebagai distributor</a>
                        </div>
                      </div>
                    </div>
                    <br/>
                  </div>
            </div>
        </div>

    <div className="white">
      <section id="ctas-footer">
          <div className="row"> 
               <a href="" className="col m6 s12 white-text purple">
                <br/>
                <div className="col s3 offset-s1"> 
                    <i className="mdi-hardware-headset large"></i>
                </div>
                <div className="col s8">
                    <h3 className="light">Hubungi kami kapan saja</h3>
                    <br/>
                </div>
               </a>
             <a href="" className="col m6 s12 green white-text">
                <br/>
              <div className="col s3 offset-s1">
                <i className="mdi-action-shopping-cart large"></i>
              </div>
              <div className="col s8">
                <h3 className="light text-left">Transaksi mudah dan cepat</h3><br/>
              </div>
             </a>
          </div>
       </section>



        <div id="content" className="testimonials section-box row lighten-5">
          <div className="container">
            <div className="center flow-text">
             <span className="blue-grey-text text-lighten-3"> Testemonials, <small><em>Apa kata mereka?.</em></small> 
            </span></div> <br/><br/>
              <ul>
                <li className="col m4 s12">
                  <div className="caption left-align">
                      <div className="col s3"> 
                      <img src="assets/images/male.png" className="circle wp-post-image" width="85" height="85"/>
                      </div>
                      <div className="col s9">
                        <p className="grey-text text-darken-3"></p>
                        <div itemprop="reviewBody">Semoga website ini menjadi jalan terbaik untuk <strong>Shemura</strong> dalam melayani para distributor kami secara online.</div> 
                        <br/><br/>
                        <p className="name" itemprop="name">Alex H.</p>
                      <div className="divider"></div>
                    </div>
                  </div>
                </li>
                <li className="col m4 s12">
                      <div className="caption left-align">
                          <div className="col s3"> 
                          <img src="assets/images/male.png" className="circle wp-post-image" alt="daniel cardoso" width="85" height="85"/></div><div className="col s9">
                          <blockquote cite="hj" itemscope="">
                          Target penjualan kami sudah semakin luas, <strong>Shemura</strong>
                           membutuhkan system seperti ini agar pelayanan distributor kami lebih mudah  
                          <a href=""> <strong>Hubungi kami</strong> </a>
                           kapan saja kami siap melayani anda.
                          
                          <br/><br/>
                          <div itemprop="author" itemscope=""><p className="name" itemprop="name">Hari H.</p></div>
                          <div className="divider"></div>
                          </blockquote>
                          </div>
                      </div>
                </li>
              <li className="col m4 s12">
                <div className="caption left-align">
                    <div className="col s3"> 
                        <img src="assets/images/female.png" className="circle wp-post-image" alt="Alexandre Solera" width="85" height="85"/>
                    </div>
                        <div className="col s9">
                           Target penjualan kami sudah semakin luas, <strong>Shemura</strong> membutuhkan system seperti ini agar pelayanan distributor kami lebih mudah <a href=""><strong>Hubungi kami</strong></a> kapan saja kami siap melayani anda.
                            <br/><br/>

                            <p className="name" itemprop="name">Andy haru.</p>

                            <div className="divider">
                      
                        </div>
                    </div>
                </div>
              </li>
          </ul>
        </div>
      </div>
  </div>

<div className="clients-area section-box hide-on-small-only lighten-5">
  <div className="content-clients-area cf content-partners">
    <div className="row cf valign-wrapper">
          <div className="col m10 s11 valign-wrapper">
                <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src="assets/images/visa.png" className="responsive-img center" title="Startup Brasil" alt="Startup Brasil"/>
                    </div>
                </div>

                <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src="assets/images/bca.png" className="responsive-img center" title="Startup Brasil" alt="Startup Brasil"/>
                    </div>
                </div>
                <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src="assets/images/bri.png" className="responsive-img center" title="Startup Brasil" alt="Startup Brasil"/>
                    </div>
                </div>
           </div>
           <div className="col m10 s11 valign-wrapper">
                 <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src="assets/images/mc.png" className="responsive-img center" title="Startup Brasil" alt="Startup Brasil"/>
                    </div>
                </div>      <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src="assets/images/discover.png" className="responsive-img center" title="Startup Brasil" alt="Startup Brasil"/>
                    </div>
                </div>      <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src="assets/images/mandiri.png" className="responsive-img center" title="Startup Brasil" alt="Startup Brasil"/>
                    </div>
                </div>
             </div>
       </div>
    </div>
</div>
</div>
    );
  }
}
 
export default Home