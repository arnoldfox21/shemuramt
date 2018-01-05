import React from 'react'


class CompanyprofileComponent extends React.Component{
    constructor(props){
       super(props);
       }
    render(){
        return(

            <div className="card-content">
                <span className="card-title grey-text text-darken-4">Hallo</span>
                  <p>{this.props.idc.about_post}
                  </p>                    
                  <p><i className="mdi-action-perm-identity cyan-text text-darken-2"></i> Gita kumalasari</p>
                  <p><i className="mdi-communication-business cyan-text text-darken-2"></i> Kec. Lawang Kab Malang</p>
                  <p><i className="mdi-action-perm-phone-msg cyan-text text-darken-2"></i> +1 (612) 222 8989</p>
                  <p><i className="mdi-communication-email cyan-text text-darken-2"></i> help@shemura-mt.com</p>  
            </div>

                )
     }

                            
}
export default CompanyprofileComponent