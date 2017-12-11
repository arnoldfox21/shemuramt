import React from 'react'

class Slider extends React.Component{

    render(){
        return(
            <div class="slider">
              <ul class="slides">
                  <li>
                        <img src="assets/images/fg.jpg"/> 
                      <div class="caption center-align">
                          <h3>Selamat datang di situs resmi</h3>
                          <h5 class="light grey-text text-lighten-3">Shemura MT</h5>
                      </div>
                  </li>
                  <li>
                      <img src="assets/images/slide2.jpg"/>
                      <div class="caption left-align">
                          <h3>Pabrik pupuk cair</h3>
                          <h5 class="light grey-text text-lighten-3">Solusi cerdas untuk petani.</h5>
                      </div>
                  </li>
                  <li>
                  <img src="assets/images/slide1.jpg"/>       
                          <div class="caption right-align">
                      <h3>Lebih efisien</h3>
                      <h5 class="light grey-text text-lighten-3">mudah dan tidak terlalu menguras tenaga.</h5>
                      </div>
                  </li>
                  <li>
                      <img src="assets/images/slide5.jpg"/> 
                      <div class="caption center-align">
                          <h3>Sistem layanan dan pelayanan yang canggih</h3>
                          <h5 class="light grey-text text-lighten-3">Here's our small slogan.</h5>
                      </div>
                  </li>
              </ul>
            </div>
            )
    }
} 
export default Slider