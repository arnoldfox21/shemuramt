import React from 'react';

class ListTestemonials extends React.Component {
	
	render(){
		return(
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


			)

	}
}
export default ListTestemonials