import React from 'react'


class Bank extends React.Component {

	render(){
		return (
			  <div className="col m6 s12 cf valign-wrapper">
                    <div className="col s10"> 
                    <img src={this.props.cover} className="responsive-img center"/>
                    </div>
                </div>

			)
	}

}
export default Bank