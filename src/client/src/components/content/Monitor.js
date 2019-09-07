import React, { Component } from 'react'
import { observer } from 'mobx-react'

import DatePicker from 'react-datepicker'
import { registerLocale } from  "react-datepicker";
import es from 'date-fns/locale/es';
import { Line } from 'react-chartjs-2';

import "./Monitor.css"
import "./ScatterChart.css"
import "react-datepicker/dist/react-datepicker.css";

registerLocale('es', es)

const Monitor = observer( class Monitor extends Component {
	constructor(props){
		super(props);
		this.chartReference = {}
		this.hideChart = false;
		this.state = {
			mostrar: false,
			data: {
				labels: [null],
				datasets: [{
					label: "Lecturas",
					data: [{
						t: null,
						y: 1
					}],
					borderWidth: 1,
					backgroundColor: "#f1bc7f"
				}]
			},
			options: {
				responsive: true,
				maintainAspectRatio: 1
			}
		}
	}
	componentDidMount(){
		console.log(this.chartReference.chartInstance)
		this.chartUpdate = setInterval(() => {
			this.setState({data: this.props.uiState.dayData});
			console.log("Update")
		}, 1000)
	}
	dateHandler = (date) => { this.props.uiState.setDay(date) }
    render() {
        return (
            <div>
                <p>El monitor visualiza todos los datos recaudados por el dispositivo durante <i>un día completo</i>, para seleccionar un día, por favor <b>clickear</b> la fecha en el recuadro.</p>
                <div className="datepicker">
                    {this.props.uiState.wrongDate ? 
						<p>Fecha errónea, por favor elegir una fecha pasada:</p> 
						: 
						<p>Seleccione la fecha:</p>
					}
                    <DatePicker
                        selected={this.props.uiState.dateSelected}
                        onChange={this.dateHandler}
                        locale="es"
                    />
					{this.props.uiState.emptyDate ?
						<p>No existen datos registrados para la fecha suministrada</p>
						:
						<button
							onClick={ () => {
								this.dateHandler(this.props.uiState.dateSelected)
							}}
						>Refrescar datos</button>
					}
                </div>
                <br/>
				{
					this.hideChart ? "" :
					<Line
						ref={(reference) => this.chartReference = reference}
						data={this.state.data}
						options={this.state.options}
					/>
				}
				<button 
					onClick={() => {
						this.chartReference.chartInstance.destroy();
						this.hideChart = true;
					}}
				>Destroy</button>
            </div>
        )
    }
})

export default Monitor