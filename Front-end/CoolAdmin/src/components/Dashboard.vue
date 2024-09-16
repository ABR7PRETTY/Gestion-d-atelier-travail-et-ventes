<script setup xmlns="http://www.w3.org/1999/html">


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div style="text-align: center; margin-bottom: 30px">
          <h1 style="color: #6f42c1; text-shadow: #9fcdff">Récement : </h1> <h3>   {{RecDesignation.mois}}-{{RecDesignation.date}}</h3>
        </div>

        <div class="row" v-for="(item, index) in ateliers" :key="index">

            <div class="col-md-4" >
              <div class="card" >
                <img class="card-img-top" style="height: 200px" :src="getUrlImage(item.image)" :alt="item.nom">
                <div class="card-body">
                  <h3>{{item.nom}}</h3>
                </div>
                </div>

              </div>
          <div class=" card " style="float: right; width: 800px; text-align: center; padding-top: 20px; background-color: #09454f ">
            <h3 style="color: #9fcdff">Travail</h3>
            <template v-for="des in designations" >
              <template v-if="des.date===RecDesignation.date && des.mois===RecDesignation.mois && des.atelier===item.nom" >
                <h3 style="color: white">{{des.travail}}</h3>
              </template>
            </template>
            <h3 style="margin-top:30px; margin-bottom:20px; color: #f171b1 ">Vente</h3>
            <table  style="color: white; margin-right: 30px; margin-left: 30px">
              <thead>
              <tr style="color:#000000 ; background-color: rgba(255,255,255,0.94)">
                <th>Quantite</th>
                <th>Article</th>
                <th>Prix</th>
              </tr>

              </thead>
              <tbody >
              <template v-for="vet in ventes" >
                <template v-if="vet.date===RecDesignation.date && vet.mois===RecDesignation.mois && vet.atelier===item.nom" >
                  <tr >
                    <td>{{vet.quantite}}</td>

                    <td>{{vet.article}}</td>

                    <td>{{vet.prix}}</td>
                  </tr>
                </template>
              </template>
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

export default {
  data(){
    return{
      RecDesignation: {},
      ateliers:[],
      designations:[],
      ventes:[],

    };
  },
  mounted() {
    this.listDesignation();
    this.listAtelier();
    this.listVente();
  },
  methods: {
    async listDesignation(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/designations')
        this.designations=response.data
        if (this.designations.length > 0) {
          this.RecDesignation = this.designations[this.designations.length - 1];
        } else {
          this.RecDesignation = {};
        }
      }catch (error){
        console.error(error)
      }
    },

    async listVente(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ventes')
        this.ventes=response.data
      }catch (error){
        console.error(error)
      }
    },

    async listAtelier() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ateliers');
        this.ateliers = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    getUrlImage(monImage) {
      return 'http://127.0.0.1:5000/static/' + monImage;
    },
    showEditModal(designation) {
      this.currentDesignation = { ...designation };
    },
  },


  props:{}
};
</script>

<style scoped>

</style>