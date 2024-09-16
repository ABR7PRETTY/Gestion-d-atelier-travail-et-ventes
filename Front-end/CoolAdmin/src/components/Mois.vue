<script setup>


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div class="row form-group" style="color: #6f42c1; font-size: 1.8em">
          <div class="col col-md-9">
            <div class="form-check-inline form-check" v-for="atelier in ateliers" :key="atelier.id">
              <input type="radio"  :value="atelier" id="inline-radio1" style="width: 30px" name="inline-radios" @change="selectAtelier(atelier)" v-model="currentAtelier" >{{atelier.nom}}
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="cc-number" class="control-label mb-1">Mois</label>
          <input  type="month" class="form-control" style="height: 50px; width: 300px" aria-required="true" aria-invalid="false" v-model="currentMois" @change="selectMois(currentMois)">
        </div>
        <div class="row">

          <div class="table-responsive table--no-card m-b-30" style="margin-top:50px; font-size: 1.9em ">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr >
                <th style="font-size: 0.8em">Travail</th>
                <th style="font-size: 0.8em">Vente</th>
                <th style="font-size: 0.8em">Total</th>
                <th style="font-size: 0.8em">Depense</th>
                <th style="font-size: 0.8em">Solde</th>
              </tr>
              </thead>
              <tbody>

                <tr >
                  <td>{{ totalTravail }}</td>
                  <td>{{ totalVente }}</td>
                  <td>{{ totalVente + totalTravail}} </td>
                  <td>{{ totalDepense }}</td>
                  <td>{{ totalVente + totalTravail - totalDepense}} </td>
                </tr>
              </tbody>


            </table>
          </div>
          <div style="margin-top:50px; font-size: 1.8em " class="table-responsive table--no-card m-b-30">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr>
                <th>Article</th>
                <th>Quantité</th>
              </tr>
              </thead>
              <tbody>

              <tr v-for="(item, index) in totalVenduParArticle" :key="index">
                <td>{{ index }}</td>
                <td>{{ item }}</td>
              </tr>

              </tbody>


            </table>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="copyright">
              <marquee style=" margin-top: 2px">
                <p style="color: rgba(102,102,102,0.89)"> @ABR7  &emsp; 00228 93 38 25 76</p>
              </marquee>
              <p>Copyright © 2018 Colorlib. All rights reserved. Template by <a href="https://colorlib.com">Colorlib</a>.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script>

import axios from 'axios'
import {computed} from "vue";

export default {
  data(){
    return{
      currentMois: localStorage.getItem('mois'),
      currentAtelier: JSON.parse(localStorage.getItem('atelier')),
      ateliers:[],
      ventes:[],
      designations:[],
      depenses:[],
    };
  },
  mounted() {
    this.listAtelier();
    this.listVente();
    this.listDesignation();
    this.listDepense();
  },
  methods: {
    async listVente(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ventes')
        this.ventes=response.data
      }catch (error){
        console.error(error)
      }
    },
    async listDesignation(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/designations')
        this.designations=response.data
      }catch (error){
        console.error(error)
      }
    },

    async listAtelier(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ateliers')
        this.ateliers=response.data
      }catch (error){
        console.error(error)
      }
    },

    async listDepense(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/depenses')
        this.depenses=response.data
      }catch (error){
        console.error(error)
      }
    },

    calculateTotalTravail() {
      return this.designations.reduce((sum, designation) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (designation.atelier === this.currentAtelier.nom && designation.mois===this.currentMois) {
          return sum + parseFloat(designation.travail || 0);
        }
        return sum; // Si la condition n'est pas remplie, on retourne la somme actuelle
      }, 0);
    },

    calculateTotalVente() {
      return this.ventes.reduce((sum, vente) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (vente.atelier === this.currentAtelier.nom && vente.mois===this.currentMois) {
          return sum + parseFloat(vente.prix || 0);
        }
        return sum; // Si la condition n'est pas remplie, on retourne la somme actuelle
      }, 0);
    },

    calculateTotalDepense() {
      return this.depenses.reduce((sum, depense) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (depense.atelier === this.currentAtelier.nom && depense.mois===this.currentMois) {
          return sum + parseFloat(depense.montant || 0);
        }
        return sum; // Si la condition n'est pas remplie, on retourne la somme actuelle
      }, 0);
    },

    calculateTotalVenduParArticle() {
      const totalVendus = {};

      this.ventes.forEach(vente => {
        if (vente.atelier === this.currentAtelier.nom && vente.mois===this.currentMois){
          const articleId = vente.article;
          const quantite = parseInt(vente.quantite, 10) || 0;

          if (totalVendus[articleId]) {
            totalVendus[articleId] += quantite;
          } else {
            totalVendus[articleId] = quantite;
          }
        }

      });

      return totalVendus;
    },

    selectAtelier(newAtelier) {
      this.currentAtelier = newAtelier;

      // Mettre à jour dans localStorage
      localStorage.setItem('atelier', JSON.stringify(this.currentAtelier));

    },

    selectMois(newMois) {
      this.currentMois = newMois;

      // Mettre à jour dans localStorage
      localStorage.setItem('mois',this.currentMois);

    },
  },


computed: {
  totalTravail() {
    return this.calculateTotalTravail();
  },
  totalVente() {
    return this.calculateTotalVente();
  },
  totalDepense() {
    return this.calculateTotalDepense();
  },
  totalVenduParArticle() {
    return this.calculateTotalVenduParArticle();
  }
},
  props:{}
};
</script>

<style scoped>

</style>