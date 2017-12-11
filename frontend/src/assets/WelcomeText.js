import React from 'react'

class WelcomeText extends React.Component{
    render(){

        return(
        <div className="col s12 banner z-depth-1 purple" id="banner_home">
            <br/>
              <h1 className="header col s12 white-text center centralize">
              Selamat datang di Situs resmi kami
               </h1>
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

            )

    }
}
export default WelcomeText