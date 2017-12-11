import React from 'react'


class ListRecentDistributor extends React.Component{

	render(){
		return(
  			    <li class="collection-item avatar">
                  <img src={"http://127.0.0.1:8000/libs/media/" + this.props.pic} className="circle" width="40" />
                  <span class="title">{this.props.name}</span>
                      <p>Bergabung di Shemura MT.
                        <br/> <span class="ultra-small">pada {this.props.jointime}</span>
                      </p>
                  <a class="secondary-content"><i class="mdi-editor-attach-money"></i></a>
                </li>
			)
	}

}
export default ListRecentDistributor