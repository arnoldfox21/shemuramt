import React, {Component} from 'react';
import SingleProduct from '../assets/Singleproduct'
import ListProductHorizontal from '../assets/ListProducthorizontal'
import LoaderPage from '../assets/LoaderComponent'
import Home from './Home'
import Axios from 'axios'

class DetailProduct extends React.Component{

	constructor(){
	    super();
	    this.state = {
	      dataOperations: [],
        isLoading: true
	    };
      var Agentx = {
        id: this.state.idf
      }
  // Axios({
  //     url: "http://127.0.0.1:8000/barang/select/",
  //     dataType: 'json',
  //     type: 'POST',
  //     data: Agentx,
  //     success: function(data) {
  //       this.setState({data: data});
  //     }.bind(this),
  //     error: function(xhr, status, err) {
  //       console.error(this.props.url, status, err.toString());
  //     }.bind(this)
  //   });
  //   Axios({
  //       url: this.props.url,
  //       dataType: 'json',
  //       cache: false,
  //       success: function(data) {
  //         this.setState({data: data});
  //       }.bind(this),
  //       error: function(xhr, status, err) {
  //         console.error(this.props.url, status, err.toString());
  //       }.bind(this)
  //     });
	}
  componentDidMount() {

    setTimeout(function() { 
        this.setState({isLoading: false}) 
      }.bind(this), 2000);

    fetch('http://127.0.0.1:8000/Selectallbarang/?format=json')
   .then(res => { 

    return res.json();
      }).then(mdata => {
         
          let dataOperations = mdata.map((idb, index) => {
            
            return(
            
                  <ListProductHorizontal pdc={idb} />   
                               
            )
          })
         this.setState({dataOperations: dataOperations});
     })

  }
 render(){
  console.log(this.state.idf)
  if(this.state.isLoading) {
      return(<LoaderPage/>)
    } else { if (this.state.idf != '') {
  return(
      <div id="main">        
        <div className="wrapper">
          <SingleProduct takeid={this.state.idf}/>    
          <div className="row white">
            <div className="col s12 m12 l12">
                 <h4 className="center-align">Produk lainnya</h4>
                 {this.state.dataOperations}
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col m12 l12 s12">
            <p className="caption">Punya pertanyaan jangan ragu untuk menghubungi kami, silahkan <a href="hub">klik disini</a> customer service kami dengan senang hati membantu anda?</p>
            <div className="divider">
            </div>
          </div>
        </div>
      </div>

  )}
  else{
    return(<h1>cc</h1>)
  }
 }
}
};

export default DetailProduct;