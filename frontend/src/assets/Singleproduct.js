import React from 'react'

class SingleProduct extends React.Component{

    render(){
        return(
            <section id="content">
                <div className="parallax-container">
                    <div className="parallax">
                        <img src="assets/images/shemura-bg.jpg"/>
                    </div>
                </div>
                <div className="container">
                    <div className="section">
                        <div className="row card">
                            <div className="col s12 m6 l6">
                                <div className="card">
                                  <div className="card-image purple waves-effect">
                                    <img src="assets/images/vg.jpg"/>
                                  </div>
                                  <div className="card-content">
                                    <ul className="collection">
                                      <li className="collection-item flow-text center-align">Pupuk cair </li>
                                      <li className="collection-item flow-text"><i className="mdi-image-nature-people prefix"></i> Berat : <div className="right"> 5kg</div></li>
                                      <li className="collection-item flow-text"><i className="mdi-editor-attach-money prefix"></i> Harga satuan :  <div className="right">Rp. .00</div></li>
                                      <li className="collection-item flow-text"><i className="mdi-maps-store-mall-directory prefix"></i> Warna : <div className="right">  merah </div></li>
                                    </ul>
                                  </div>
                                </div>
                            </div>
                            <div className="col s12 m6 l6">
                                <p className="flow-text">Harga produk pupuk cair bisa berubah kapan saja tanpa pemberitahuan sebelumnya, kecuali yang tercantum dalam fakthur pemesanan</p>
                                <div id="multi-color-tab" className="section">
                                    <div className="row">
                                        <div className="col s12">
                                            <ul className="tabs tab-demo-active z-depth-1">
                                              <li className="tab col s3"><a className="white-text red darken-1 waves-effect waves-light" href="#sapien1"><i className="mdi-action-perm-identity"></i> Stock</a>
                                              </li>
                                              <li className="tab col s3"><a className="white-text darken-1 waves-effect waves-light active purple" href="#activeone1"><i className="mdi-action-settings-display"></i> Kelebihan</a>
                                              </li>
                                              <li className="tab col s3"><a className="white-text light-blue darken-1 waves-effect waves-light" href="#vestibulum1"><i className="mdi-action-speaker-notes"></i> Kekuranagn</a>
                                              </li>
                                            </ul>
                                        </div>
                                        <div className="col s12">
                                            <div className="col l4 m4 s12">
                                                <p className="flow-text"><center><b>45</b> Tersedia</center></p>
                                            </div>
                                        <div className="col l4 m4 s12">
                                          <dl>
                                            <dt><center><b>Praktis</b></center></dt>
                                          </dl>
                                        </div>
                                            <div className="col l4 m4 s12">
                                              <p><center><b>mudah terbakar </b></center></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <form className="col s12" method="POST">
                                    <div className="row">
                                        <div className="input-field col s12 l4 m4">
                                            <input id="n" type="hidden" name="id_barang" className="validate" value=""/>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="input-field col s12 l4 m4">
                                            <input id="age_input1" type="number" name="jumlah" className="validate" value="1"/>
                                                <label for="age_input1" data-error="Silahkan masukkan jumlah.">Jumlah</label>
                                        </div>
                                    </div>
                                    <div className="row">
                                        <div className="row">
                                            <div className="card-action center-align">                      
                                                <button disabled type="submit" className="purple waves-effect waves-light btn">Tambah ke keranjang</button>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                                </div>
                            </div>
                        </div>
                    </div>            
                </section>
            )
    }
}
export default SingleProduct