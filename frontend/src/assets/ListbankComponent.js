import React from 'react'
import Bank from './ListBank'

class ListBank extends React.Component{
	render(){
		console.log(this.props)
		return(

			<div className="clients-area section-box hide-on-small-only lighten-5">
			  <div className="content-clients-area cf content-partners">
			    <div className="row cf valign-wrapper">
				
			          <div className="col m12 s12 valign-wrapper">
			          {this.props.Dep.map( (dept) => {
			          	return(
			              <Bank name={dept.name} cover={dept.logo} />
			                	 )

			                 })
			             }
			             </div>
			       </div>
			    </div>
			</div>

			)


	}



}

export default ListBank