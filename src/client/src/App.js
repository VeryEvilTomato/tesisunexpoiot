import React, { Component } from 'react'

import NavBar from './components/nav/NavBar'
import Content from './components/content/Content'

import './App.css';
import './button.css';
import { observer } from 'mobx-react';

const App = observer(class App extends Component {
	render() {
		return (
			<div className='Main'>
				<header>Universidad Nacional Experimental Politécnica “Antonio José de Sucre” Vicerrectorado Puerto Ordaz</header>
				<div className='app'>
					<NavBar 
						className='app' 
						uiState={this.props.uiState}
					/>
					{this.props.uiState.content === null ?
						<div className="welcome">
							<p>Bienvenidos a Tomate IoT</p>
						</div>
						:
						<Content
							uiState={this.props.uiState}
						/>
					}
				</div>
			</div>
		)
	}
})

export default App;