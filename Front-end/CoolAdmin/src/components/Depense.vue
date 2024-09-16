<script setup xmlns="http://www.w3.org/1999/html">


</script>

<template>
  <div class="main-content">
    <div class="section__content section__content--p30">
      <div class="container-fluid">
        <div class="row form-group" style="color: #6f42c1; font-size: 1.8em">
          <div class="col col-md-9">
            <div class="form-check-inline form-check" v-for="atelier in ateliers" :key="atelier.id">
              <input type="radio"  :value="atelier" id="inline-radio1" style="width: 30px" name="inline-radios"  v-model="currentAtelier" @change="selectAtelier(atelier)">{{atelier.nom}}
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="cc-number" class="control-label mb-1">Mois</label>
          <input  type="month" class="form-control" style="height: 50px; width: 300px" aria-required="true" aria-invalid="false" v-model="currentMois" @change="selectMois(currentMois)">


        </div>
        <button type="button" class="btn btn-outline-success btn-lg" style="margin-bottom:70px; font-size: 1.8em" @click="this.depense.atelier_id=this.currentAtelier.id ; this.depense.mois=this.currentMois" data-toggle="modal" data-target="#Add"><i class="fa fa-plus-square"></i> Ajouter</button>
        <div class="row">

          <div class="table-responsive table--no-card m-b-30">
            <table class="table table-borderless table-striped table-earning">
              <thead >
              <tr>
                <th>Date</th>
                <th>Montant</th>
                <th>Motif</th>
                <th>Action</th>
              </tr>
              </thead>
              <tbody>


              <template v-for="item in depenses" >
                <tr style="font-size: 1.5em" v-if=" item.atelier === currentAtelier.nom &&  item.mois === currentMois">
                  <td>{{ item.date }}</td>
                  <td>{{ item.montant }}</td>
                  <td>{{ item.motif }}</td>
                  <td>
                    <i class="fa fa-pencil-alt" style="font-size: 1.1em; color: #c69500; margin-right: 20px" @click="showEditModal(item); this.currentDepense.atelier_id=this.currentAtelier.id" data-toggle="modal" data-target="#Edit"></i>
                    <i class="fa fa-trash-alt" style="font-size: 1.1em; color: #bd2130" @click="deleteDepense(item.id)"></i>
                  </td>
                </tr>
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


  <div class="modal fade" id="Add" tabindex="-1" role="dialog" aria-labelledby="mediumModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="mediumModalLabel">Depense</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Nouvelle Depense</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="addDepense">
                  <div class="form-group">
                    <label  class="control-label mb-1">Date</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="depense.date">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Montant</label>
                    <input  type="number" class="form-control cc-name valid" v-model="depense.montant">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Motif</label>
                    <input  type="text" class="form-control cc-name valid" v-model="depense.motif">
                  </div>
                  <div v-if="Message" class="alert alert-success">
                    {{ Message }}
                  </div>
                  <div v-if="errorMessage" class="alert alert-danger">
                    {{ errorMessage }}
                  </div>
                  <div class="modal-footer" style="margin-right: 130px">
                    <i class="fa fa-reply"  style="font-size: 3em; color: #bd2130; margin-right: 100px" data-dismiss="modal"><h4>Retour </h4></i>
                    <button type="submit" > <i class="fa fa-check"  style="font-size: 3em; color: #00b26f" ><h4>Save </h4> </i> </button>
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
          <h5 class="modal-title" id="mediumModalLabel">Depense</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" style="margin-left: 100px">
          <div class="col-lg-10">
            <div class="card">
              <div class="card-header" style="color: white; background-color: #6f42c1">Modification Depense</div>
              <div class="card-body">
                <div class="card-title">
                  <h3 class="text-center title-2" style="color: #6f42c1">Veuillez remplir les champs</h3>
                </div>
                <hr>
                <form  @submit.prevent="editDepense(currentDepense.id)">
                  <div class="form-group">
                    <label  class="control-label mb-1">Date</label>
                    <input  type="number" class="form-control" aria-required="true" aria-invalid="false" v-model="currentDepense.date">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Mois</label>
                    <input  type="month" class="form-control" aria-required="true" aria-invalid="false" v-model="currentDepense.mois">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Montant</label>
                    <input  type="number" class="form-control cc-name valid" v-model="currentDepense.montant">
                  </div>
                  <div class="form-group has-success">
                    <label  class="control-label mb-1">Motif</label>
                    <input  type="text" class="form-control cc-name valid" v-model="currentDepense.motif">
                  </div>
                  <div class="form-group">
                    <label for="cc-number" class="control-label mb-1">Atelier</label>
                    <select class="form-control" v-model="currentDepense.atelier_id">
                      <option v-for="atelier in ateliers" :key="atelier.id" :value="atelier.id">
                        {{ atelier.nom }}
                      </option>
                    </select>
                  </div>
                  <div v-if="ModiferrorMessage" class="alert alert-danger">
                    {{ ModiferrorMessage }}
                  </div>
                  <div v-if="ModifMessage" class="alert alert-success">
                    {{ ModifMessage }}
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
      depense:{
        date:'',
        montant:'',
        motif:'',
        atelier_id:'',
        mois:'',
      },
      currentDepense: {},
      currentAtelier: JSON.parse(localStorage.getItem('atelier')),
      currentMois: localStorage.getItem('mois'),
      RecDepense: {},
      ateliers:[],
      depenses:[],
      Message: null,
      errorMessage: null,
      ModifMessage: null,
      ModiferrorMessage: null,
    };
  },
  mounted() {
    this.listDepense();
    this.listAtelier();
  },
  methods: {
    async listDepense(){
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/michelin/depenses')
        this.depenses=response.data
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
    async addDepense() {
      this.depense.atelier_id=this.currentAtelier.id
      this.depense.mois=this.currentMois
      if(0<this.depense.date && this.depense.date<=31 && this.depense.montant>0){
        const formData = new FormData();
        formData.append('date', this.depense.date);
        formData.append('montant', this.depense.montant);
        formData.append('motif', this.depense.motif);
        formData.append('atelier_id', this.depense.atelier_id);
        formData.append('mois', this.depense.mois);

        try {
          await axios.post('http://127.0.0.1:5000/api/michelin/depenses', formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.Message="Enregistrement reussi"
          this.errorMessage=null
          this.depense = {};
          await this.listDepense();
        } catch (error) {
          console.error('Error:', error);
        }
      }else{
        this.Message=null
        this.errorMessage="Date ou Montant incorrect"
      }

    },
    async editDepense(id) {
      if(0<this.currentDepense.date && this.currentDepense.date<=31 && this.currentDepense.montant>0){
        const formData = new FormData();
        formData.append('date', this.currentDepense.date);
        formData.append('montant', this.currentDepense.montant);
        formData.append('motif', this.currentDepense.motif);
        formData.append('atelier_id', this.currentDepense.atelier_id)
        formData.append('mois', this.currentDepense.mois)

        try {
          await axios.put(`http://127.0.0.1:5000/api/michelin/updateDepense/${id}`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
          });
          this.ModiferrorMessage=null
          this.ModifMessage="Modification reussi"
          this.currentDepense = {};
          await this.listDepense();
        } catch (error) {
          console.error('Error:', error);
        }
      }
      else{
        this.ModifMessage=null
        this.ModiferrorMessage = 'Date ou montant Incorrect';

      }
    },
    async deleteDepense(id) {
      try {
        await axios.delete(`http://127.0.0.1:5000/api/michelin/deleteDepense/${id}`);
        await this.listDepense();
      } catch (error) {
        console.error(error);
      }
    },
    showEditModal(depense) {
      this.currentDepense = { ...depense };
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


  props:{}
};
</script>

<style scoped>

</style>