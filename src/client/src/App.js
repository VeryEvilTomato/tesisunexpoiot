import React, { Component } from 'react'

import NavMenu from './components/nav/NavMenu'

import './App.css';

export default class App extends Component {
	constructor(props) {
		super(props);
		this.contentHandler = this.contentHandler.bind(this);
		this.logoffHandler = this.logoffHandler.bind(this);
		this.state = {
			content: null
		}
	}
	contentHandler(section) {
        this.setState({ content: section })
	}
	logoffHandler = () => {
		console.log("La sección es: " + this.state.content)
        // console.log("Su sesión ha sido cerrada")
    }
	render() {
		return (
			<main>
				<header>Universidad Nacional Experimental Politécnica “Antonio José de Sucre” Vicerrectorado Puerto Ordaz</header>
				<div className='container'>
					<div className='nav'>
						<img src="/images/unexpo_logo.png" alt="Logo UNEXPO" />
						<NavMenu 
							contentHandler={this.contentHandler}
							logoffHandler={this.logoffHandler}
						/>
					</div>
				<div className='content'>
					Nisi id irure exercitation cillum dolore. Aliqua ut aliquip aliqua culpa ipsum qui laborum dolore excepteur velit in. Fugiat ullamco cupidatat cupidatat proident ut. Velit minim ex ipsum in veniam. Cupidatat in magna proident ex ea voluptate sint cupidatat tempor ad nisi amet. Esse magna reprehenderit quis do irure proident. Est nisi anim qui enim magna sint pariatur consectetur sunt in enim non. Ullamco consequat Lorem eu commodo.
         	 	</div>
					<div className='sidebar'> Pariatur ipsum elit aliquip reprehenderit amet voluptate.</div>
				</div>
			</main>
		)
	}
}