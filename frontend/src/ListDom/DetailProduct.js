import React, {Component} from 'react';
import SingleProduct from '../assets/Singleproduct'
import ListProductHorizontal from '../assets/ListProducthorizontal'
import LoaderPage from '../assets/LoaderComponent'
import axios from 'axios'

class DetailProduct extends React.Component{

	constructor(){
	    super();
	    this.state = {
	      dataOperations: [],
        dataSelection:[],
        isLoading: true,
        ids: localStorage.getItem('idselectitem')
	    };
	}
  componentDidMount() {

    const URL = 'http://127.0.0.1:8000/items/select/';
    return axios({
      method: 'POST',
      url: URL,
      headers: {
        'Content-Type': 'application/json'
      },
      data: {
        id: 2
      },
    })
    .then(res => {
      console.log('Data', res.data);
     })
    .catch(error => {
      console.log('Error', error.response.data);
     })

    // axios.post('http://127.0.0.1:8000/barang/select/', { id: this.state.ids })
    // .then(result =>{
    //   return result.json();
    // }).then(data => {
    //   let dataSelection = data.map((idsel, index) =>{
    //     console(data)
    //     return(

    //       <SingleProduct takeid={idsel} />    
          
    //       )
    //   })
    //   this.setState({dataSelection: dataSelection});
    // })

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

  if(this.state.isLoading) {
      return(<LoaderPage/>)
    } else { if (this.state.idf != '') {
  return(
      <div id="main">        
        <div className="wrapper">
        {this.state.dataSelection}
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
    return(<h1><center>Please select the item</center></h1>)
  }
 }
}
};

export default DetailProduct;