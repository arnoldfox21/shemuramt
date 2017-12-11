import React from 'react'

class ListProductHorizontal extends React.Component {
    
    render(){

        return(

            <div className="blog col m2 l2">
                <div className="card z-depth-2">
                    <div className="card-image waves-effect waves-block waves-light">
                      <a href="#"><img src="assets/images/vg.jpg" alt="blog-img"/></a>
                    </div>
                        <ul className="card-action-buttons">
                          <li>
                          <a href="pemesanan?id=" className="btn-floating btn-large waves-effect waves-light green accent-4">
                          <i className="mdi-action-shopping-cart"></i></a>
                          </li>                            
                        </ul>
                    <div className="card-content">
                        <p className="row">
                        <span className="left"><a href="">{this.props.pdc.nm_barang}</a></span>
                        <span className="right">jumat 67 77</span>
                        </p>
                        <h4 className="card-title grey-text text-darken-4">
                        <a href="#" className="grey-text text-darken-4">{this.props.pdc.nm_barang}</a>
                        </h4>
                        <p className="blog-post-content">Pupuk cair {this.props.pdc.nm_barang}.</p>
                    </div>
                </div>
            </div>
        )
    }
}
export default ListProductHorizontal