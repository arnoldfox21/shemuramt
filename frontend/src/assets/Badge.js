import React from 'react'

class Badge extends React.Component{

    render(){
        return(
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
            )
    }

}
export default Badge