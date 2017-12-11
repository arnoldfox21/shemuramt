import React, { Component } from 'react'
import Alias from '../actions/SendParameters'
import ListTestemonials from '../assets/ListTestemonialsComponent'
import ListBank from '../assets/ListbankComponent'
import Recentdist from '../assets/RecentDistributorComponent'
import Slider from '../assets/SliderComponent'
import Badge from '../assets/Badge'
import WelcomeText from '../assets/WelcomeText'
import LoaderPage from '../assets/LoaderComponent'


class Home extends React.Component {

  constructor(){
    
    super();
    this.state = {
      dataOperations: [],
      distributorOperations: [],
      isLoading: true
    };
  }

  idFor(e) {
    this.state = {
      idf: e
    };
   window.location = "#/detail";
  }

  componentDidMount(){
    setTimeout(function() { 
        this.setState({isLoading: false}) 
      }.bind(this), 2000);

    fetch('http://127.0.0.1:8000/alldistributor/?format=json')
   .then(res => { 

    return res.json();
      }).then(mdata => {
     
          let distributorOperations = mdata.map((idb, index) => {
            return(
             
                  <Recentdist join={idb} />   
                               
            )
          })
         this.setState({distributorOperations: distributorOperations});
   })


    fetch('http://127.0.0.1:8000/Selectallbarang/?format=json')
   .then(results => { 

    return results.json();
      }).then(data => {

          let dataOperations = data.map((idk, index) => {
            return(

                  <div className="blog col m4 l4 margin_bottom20px">
                      <div className="card z-depth-2">
                          <div className="card-image waves-effect waves-block waves-light">
                              <a href="pemesanan?id=">
                                <img src="assets/images/vg.jpg" alt="blog-img"/>
                              </a>
                          </div>
                          <ul className="card-action-buttons">
                              <li>
                                <button onClick={(e)=>this.idFor(idk.id)} className="btn-floating btn-large waves-effect waves-light green accent-4"><i className="mdi-action-shopping-cart"></i></button>
                              </li>                            
                          </ul>
                          <div className="card-content">
                              <p className="row">
                                <span className="left"><a href="">{idk.nm_barang}</a></span>
                                <span className="right">2017</span>
                              </p>
                              <h4 className="card-title grey-text text-darken-4"><a href={idk.id} onClick={(e)=>this.idFor("1")} className="grey-text text-darken-4">{idk.nm_barang}</a>
                              </h4>
                              <p className="blog-post-content">Pupuk cair {idk.nm_barang}.</p>
                              
                          </div>
                      </div>
                  </div>
                  
              )
          })
         this.setState({dataOperations: dataOperations});
        })
      }

  render() {
      const BANK = [
            {id: 1, name: "visa", logo: "assets/images/visa.png"}, 
            {id: 2, name: "bca", logo: "assets/images/bca.png"},
            {id: 1, name: "bri", logo: "assets/images/bri.png"}, 
            {id: 2, name: "mastercard", logo: "assets/images/mc.png"},
            {id: 1, name: "discover", logo: "assets/images/discover.png"},
            {id: 2, name: "mandiri", logo: "assets/images/mandiri.png"}
            ]
    if(this.state.isLoading) {
      return(<LoaderPage/>)
    } else {
    return (
    <div>             
        
        <Slider/>       

       <WelcomeText />
    <div id="main">
      <div className="wrapper card">
        <section id="content">              
          <div className="container">
            <div className="section">
              <div className="row">
                <div className="col s12 m9 l9">
                  {this.state.dataOperations}
                </div>
                    <div id="profile-page-sidebar" className="col s12 m3"> 
                        <div className="card darken-2 purple">
                          <div className="card-content white-text center-align">
                            <p className="card-title"><i className="mdi-social-group-add"></i> 426</p>
                            <p>Distributor terbaru</p>
                          </div>                  
                          </div>
                            <ul id="profile-page-about-feed" className="collection z-depth-1">
                                {this.state.distributorOperations}
                            </ul>
                          </div>
                       </div>
                     </div>
                  </div>
          </section>
        </div>
      </div>
        <div className="white">
            <Badge/>
            <ListTestemonials/>
        </div>
            <ListBank Dep={BANK}/>
        </div>
      );
    }
  }
}
 
export default Home