import React from 'react'
import ListRecentDistributor from './RecentDistributor'

class Recentdist extends React.Component{
    render(){

        return (
            
                <li class="collection-item avatar">
                <img src={"http://127.0.0.1:8000/libs/media/" + this.props.join.foto} className="circle" width="40" />
                <span class="title">{this.props.join.nama}</span>
                    <p>Bergabung di Shemura MT.
                   <br/> <span class="ultra-small">pada {this.props.join.joined_time}</span>
                    </p>
                <a class="secondary-content"><i class="mdi-editor-attach-money"></i></a>
              </li>
         
        )
    }

} 
export default Recentdist