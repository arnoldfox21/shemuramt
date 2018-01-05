import React from 'react'

class Alert extends React.Component {
	constructor(props){
		super(props)
	}
	render(){
		return(
			<div className="row margin">
			    <div className="center">
					<div id="card-alert" class="card red">
                        <div class="card-content white-text">
                          <p><i class="mdi-alert-error"></i> {this.props.status.data.nama} </p>
                        </div>
                        <button type="button" class="close white-text" data-dismiss="alert" aria-label="Close">
                          <span aria-hidden="true">×</span>
                        </button>
                      </div>
			    </div>
			</div>
			)
	}
}
export default Alert