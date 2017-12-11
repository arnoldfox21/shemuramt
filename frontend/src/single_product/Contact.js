import React, { Component } from "react";

 
class Contact extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: true
    }
  }

  componentDidMount() {
    setTimeout(function() { 
      this.setState({isLoading: false}) 
    }.bind(this), 3000);
    
  }

  renderContact() {
    if(this.state.isLoading) {
      return(<p>Ladoing . . .</p>)
    } else {
      return (
        <div>
          <h2>GOT QUESTIONS?</h2>
          <p>The easiest thing to do is post on our <a href="http://forum.kirupa.com">forums</a>.</p>
        </div>
      )
    }
  }

  render() {
    return (
      <div>
       {this.renderContact()}
      </div>
    );
  }
}
 
export default Contact