<script setup>


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <button type="button" class="btn btn-outline-success btn-lg" style="margin-bottom:70px; font-size: 1.8em" data-toggle="modal" data-target="#Add"><i class="fa fa-plus-square"></i> Ajouter</button>
        <div class="row">

          <div class="col-md-4" v-for="(item, index) in ateliers" :key="index" >
            <div class="card" >
              <img class="card-img-top" style="height: 350px" :src="getUrlImage(item.image)" :alt="item.nom" @click="currentAtelier=item" data-toggle="modal" data-target="#Show">
              <div class="card-body">
                <h3>{{item.nom}}</h3>
                <p>{{item.localisation}}</p>
                <div class="row" style="float: right ; margin-right: 20px">
                  <i class="fa fa-pencil-alt"  style="font-size: 1.8em; color: #c69500; margin-right: 20px" @click="showEditModal(item)" data-toggle="modal" data-target="#Edit"></i>
                  <i class="fa fa-trash-alt"  style="font-size: 1.8em; color: #bd2130" @click="deleteAtelier(item.id)"></i>
                </div>
              </div>
            </div>
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


  <div class="modal fade" id="Show" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Atelier</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 40px; margin-right: 40px ">
          <div class="col-lg-12" style="text-align: center">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">{{currentAtelier.nom}}</div>
              <div class="card-body">
                <div style=" text-align: center; margin-bottom: 70px">
                  <i class="fa fa-user" style="font-size: 5em; color: #5bc0de"></i>
                  <p style="font-size: 1.3em; color: #0040e5; font-family: Rockwell  "> Responsable </p>
                  <template v-for="item in apprentis">
                    <template v-if="item.grade==='Senior' && item.atelier===currentAtelier.nom">
                      <h4 style="font-family: Bahnschrift; font-size: 1.7em"> {{item.nom}} </h4>
                    </template>
                  </template>

                </div>

                <div style=" text-align: center; margin-bottom: 60px">
                  <i class="fa fa-users" style="font-size: 5em; color: #363977"></i>
                  <p style="font-size: 1.3em; color: rgba(54,80,62,0.92); font-family: Rockwell  "> Apprentis</p>
                  <h3> {{totalApprenti}} </h3>
                </div>

                <div class="row">
                <div style="margin-left: 40px">
                  <i class="fa fa-cogs" style="font-size: 3em; color: #7d8300"></i>
                  <p style="font-size: 1.3em; color: #dcd929; font-family: Rockwell  "> Travail</p>
                  <h4> {{totalTravail}} </h4>
                </div>
                <div style="margin-left: 60px">
                  <i class="fa fa-tasks" style="font-size: 3em; color: #530191;"></i>
                  <p style="font-size: 1.3em; color: #6529dc; font-family: Rockwell  "> Vente </p>
                  <h4> {{totalVente}} </h4>
                </div>
                  <div style="margin-left: 60px">
                    <i class="fa fa-plus-square" style="font-size: 3em; color: #910117;"></i>
                    <p style="font-size: 1.3em; color: #dc29a3; font-family: Rockwell  "> Total </p>
                    <h4> {{totalTravail + totalVente}} </h4>
                  </div>
                  <div style="margin-left: 60px">
                    <i class="fa fa-ticket-alt" style="font-size: 3em; color: #ff590b; margin-left: 10px;"></i>
                    <p style="font-size: 1.3em; color: #dc7429;  font-family: Rockwell  "> Depense </p>
                    <h4 style="text-align: center"> {{totalDepense}} </h4>
                  </div>
                  <div style="margin-left: 60px">
                    <i class="fa fa-money-bill-alt" style="font-size: 3em; color: #5cff0b;"></i>
                    <p style="font-size: 1.3em; color: #a9dc29; font-family: Rockwell  "> Solde </p>
                    <h4> {{totalTravail + totalVente - totalDepense}} </h4>
                  </div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>


  <div class="modal fade" id="Add" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Atelier</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvelle Atelier</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addAtelier">
                  <div class="form-group">
                    <label  class="control-label mb-1">Libelle</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="atelier.nom">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Localisation</label>
                    <input  type="text" class="form-control cc-name valid" v-model="atelier.localisation">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Image</label>
                    <input  type="file" class="form-control cc-number identified visa" @change="onImageChange">
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Cancel </h4></i>
                    <button type="submit"> <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="Edit" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Atelier</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Atelier</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editAtelier(currentAtelier.id)">
                  <div class="form-group">
                    <label  class="control-label mb-1">Libelle</label>
                    <input  type="text" class="form-control" aria-required="true" aria-invalid="false" v-model="currentAtelier.nom">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Localisation</label>
                    <input  type="text" class="form-control cc-name valid" v-model="currentAtelier.localisation">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Image</label>
                    <input  type="file" class="form-control cc-number identified visa" @change="OnImageChangeEdit" accept="image/*">
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Cancel </h4></i>
                    <button type="submit"> <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
                  </div>
                </form>
              </div>
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
      atelier:{
        nom:'',
        localisation:'',
        image: null,
      },
      currentAtelier: {},
      ateliers:[],
      ChoixAtelier: '',
      apprentis:[],
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
    this.listApprenti();
  },
  methods: {
    onImageChange(event){
      this.atelier.image=event.target.files[0];
    },
    OnImageChangeEdit(event){
      this.currentAtelier.image=event.target.files[0];
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
    async listApprenti(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/apprentis')
        this.apprentis=response.data
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
    async listVente(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/ventes')
        this.ventes=response.data
      }catch (error){
        console.error(error)
      }
    },
    getUrlImage(monImage) {
      return 'http://127.0.0.1:5000/static/' + monImage;
    },
    async addAtelier() {
      const formData = new FormData();
      formData.append('nom', this.atelier.nom);
      formData.append('localisation', this.atelier.localisation);
      formData.append('image', this.atelier.image);

      try {
        await axios.post('http://127.0.0.1:5000/api/michelin/ateliers', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.atelier = { nom: '', localisation: '', image: null };
        await this.listAtelier();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async editAtelier(id) {
      const formData = new FormData();
      formData.append('nom', this.currentAtelier.nom);
      formData.append('localisation', this.currentAtelier.localisation);
      if (this.currentAtelier.image) {
        formData.append('image', this.currentAtelier.image);
      }

      try {
        await axios.put(`http://127.0.0.1:5000/api/michelin/updateAtelier/${id}`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.currentAtelier = {};
        await this.listAtelier();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async deleteAtelier(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteAtelier/${id}`);
        await this.listAtelier();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(atelier) {
      this.currentAtelier = { ...atelier };
    },
    calculateTotalTravails() {
      return this.designations.reduce((sum, designation) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (designation.atelier === this.currentAtelier.nom) {
          return sum + parseFloat(designation.travail || 0);
        }
        return sum; // Si la condition n'est pas remplie, on retourne la somme actuelle
      }, 0);
    },

    calculateTotalVentes() {
      return this.ventes.reduce((sum, vente) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (vente.atelier === this.currentAtelier.nom) {
          return sum + parseFloat(vente.prix || 0);
        }
        return sum; // Si la condition n'est pas remplie, on retourne la somme actuelle
      }, 0);
    },

    calculateTotalDepenses() {
      return this.depenses.reduce((sum, depense) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (depense.atelier === this.currentAtelier.nom) {
          return sum + parseFloat(depense.montant || 0);
        }
        return sum; // Si la condition n'est pas remplie, on retourne la somme actuelle
      }, 0);
    },

    calculateTotalApprentis() {
      return this.apprentis.reduce((count, apprenti) => {
        // Vérifie si l'atelier de la désignation correspond à l'atelier courant
        if (apprenti.atelier === this.currentAtelier.nom) {
          return count + 1; // Incrémente le compteur si la condition est remplie
        }
        return count; // Si la condition n'est pas remplie, on retourne le compteur actuel
      }, 0);
    },

  },


computed: {
  totalTravail() {
    return this.calculateTotalTravails();
  },
  totalVente() {
    return this.calculateTotalVentes();
  },
  totalDepense() {
    return this.calculateTotalDepenses();
  },
  totalApprenti() {
    return this.calculateTotalApprentis();
  },
},


  props:{}
};
</script>

<style scoped>

</style>