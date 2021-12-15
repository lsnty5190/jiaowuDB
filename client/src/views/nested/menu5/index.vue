<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>SECTION</h1>
        <hr><br><br>
        <alert v-if="showMessage" :message="message" />
        <button v-b-modal.book-modal type="button" class="btn btn-success btn-sm">Add</button>
        &nbsp;
        <button v-b-modal.search-modal type="button" class="btn btn-success btn-sm">Search</button>
        &nbsp;
        <button type="button" class="btn btn-success btn-sm" @click="getBooks()">Flush</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">COURSE_ID</th>
              <th scope="col">SEC_ID</th>
              <th scope="col">YEAR_SEMESTER</th>
              <th scope="col">CLASSROOM_ID</th>
              <th scope="col">TIME_SLOT_ID</th>
              <th scope="col">ENROLLMENT</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.course_id }}</td>
              <td>{{ book.sec_id }}</td>
              <td>{{ book.year_semester }}</td>
              <td>{{ book.classroom_id }}</td>
              <td>{{ book.time_slot_id }}</td>
              <td>{{ book.enrollment }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    v-b-modal.book-update-modal
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editBook(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      id="book-modal"
      ref="addBookModal"
      title="Add a new section"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="course_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addBookForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-sec-group"
          label="sec_id:"
          label-for="form-sec-input"
        >
          <b-form-input
            id="form-sec-input"
            v-model="addBookForm.sec_id"
            type="text"
            required
            placeholder="Enter Sec_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-ys-group"
          label="year_semester:"
          label-for="form-ys-input"
        >
          <b-form-input
            id="form-ys-input"
            v-model="addBookForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>

        <b-form-group
          id="form-cr-group"
          label="classroom_id:"
          label-for="form-cr-input"
        >
          <b-form-input
            id="form-cr-input"
            v-model="addBookForm.classroom_id"
            type="text"
            required
            placeholder="Enter Classroom_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-ts-group"
          label="time slot:"
          label-for="form-ts-input"
        >
          <b-form-input
            id="form-ts-input"
            v-model="addBookForm.time_slot_id"
            type="text"
            required
            placeholder="Enter Time Slot"
          />
        </b-form-group>

        <b-form-group
          id="form-enrl-group"
          label="enrollment:"
          label-for="form-enrl-input"
        >
          <b-form-input
            id="form-enrl-input"
            v-model="addBookForm.enrollment"
            type="text"
            required
            placeholder="Enter Enrollment"
          />
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal
      id="book-update-modal"
      ref="editBookModal"
      title="Update"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmitUpdate" @reset="onResetUpdate">
        <b-form-group
          id="form-title-group"
          label="course_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="editForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-sec-group"
          label="sec_id:"
          label-for="form-sec-input"
        >
          <b-form-input
            id="form-sec-input"
            v-model="editForm.sec_id"
            type="text"
            required
            placeholder="Enter Sec_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-ys-group"
          label="year_semester:"
          label-for="form-ys-input"
        >
          <b-form-input
            id="form-ys-input"
            v-model="editForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>

        <b-form-group
          id="form-cr-group"
          label="classroom_id:"
          label-for="form-cr-input"
        >
          <b-form-input
            id="form-cr-input"
            v-model="editForm.classroom_id"
            type="text"
            required
            placeholder="Enter Classroom_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-ts-group"
          label="time slot:"
          label-for="form-ts-input"
        >
          <b-form-input
            id="form-ts-input"
            v-model="editForm.time_slot_id"
            type="text"
            required
            placeholder="Enter Time Slot"
          />
        </b-form-group>

        <b-form-group
          id="form-enrl-group"
          label="enrollment:"
          label-for="form-enrl-input"
        >
          <b-form-input
            id="form-enrl-input"
            v-model="editForm.enrollment"
            type="text"
            required
            placeholder="Enter Enrollment"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal
      id="search-modal"
      ref="searchBookModal"
      title="Search student"
      hide-footer
    >
      <b-form class="w-100" @submit="onSearch" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="course_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="searchForm.course_id"
            type="text"
            required
            placeholder="Enter Course_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-sec-group"
          label="sec_id:"
          label-for="form-sec-input"
        >
          <b-form-input
            id="form-sec-input"
            v-model="searchForm.sec_id"
            type="text"
            required
            placeholder="Enter Sec_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-ys-group"
          label="year_semester:"
          label-for="form-ys-input"
        >
          <b-form-input
            id="form-ys-input"
            v-model="searchForm.year_semester"
            type="text"
            required
            placeholder="Enter Year Semester"
          />
        </b-form-group>

        <b-form-group
          id="form-cr-group"
          label="classroom_id:"
          label-for="form-cr-input"
        >
          <b-form-input
            id="form-cr-input"
            v-model="searchForm.classroom_id"
            type="text"
            required
            placeholder="Enter Classroom_ID"
          />
        </b-form-group>

        <b-form-group
          id="form-ts-group"
          label="time slot:"
          label-for="form-ts-input"
        >
          <b-form-input
            id="form-ts-input"
            v-model="searchForm.time_slot_id"
            type="text"
            required
            placeholder="Enter Time Slot"
          />
        </b-form-group>

        <b-form-group
          id="form-enrl-group"
          label="enrollment:"
          label-for="form-enrl-input"
        >
          <b-form-input
            id="form-enrl-input"
            v-model="searchForm.enrollment"
            type="text"
            required
            placeholder="Enter Enrollment"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

  </div>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert.vue'

export default {
  components: {
    alert: Alert
  },
  data() {
    return {
      books: [],
      addBookForm: {
        course_id: '',
        sec_id: '',
        year_semester: '',
        classroom_id: '',
        time_slot_id: '',
        enrollment: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        course_id: '',
        sec_id: '',
        year_semester: '',
        classroom_id: '',
        time_slot_id: '',
        enrollment: ''
      },
      searchForm: {
        course_id: '',
        sec_id: '',
        year_semester: '',
        classroom_id: '',
        time_slot_id: '',
        enrollment: ''
      }
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/sections'
      axios.get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/sections'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Student added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/sections/search'
        axios.post(path, payload)
            .then((res) => {
                this.books = res.data.books
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            })
    },
    initForm() {
      this.addBookForm.course_id = ''
      this.addBookForm.sec_id = ''
      this.addBookForm.year_semester = ''
      this.addBookForm.classroom_id = ''
      this.addBookForm.time_slot_id = ''
      this.addBookForm.enrollment = ''

      this.editForm.course_id = ''
      this.editForm.sec_id = ''
      this.editForm.year_semester = ''
      this.editForm.classroom_id = ''
      this.editForm.time_slot_id = ''
      this.editForm.enrollment = ''

      this.searchForm.course_id = ''
      this.searchForm.sec_id = ''
      this.searchForm.year_semester = ''
      this.searchForm.classroom_id = ''
      this.searchForm.time_slot_id = ''
      this.searchForm.enrollment = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        course_id: this.addBookForm.course_id,
        sec_id: this.addBookForm.sec_id,
        year_semester: this.addBookForm.year_semester,
        classroom_id: this.addBookForm.classroom_id,
        time_slot_id: this.addBookForm.time_slot_id,
        enrollment: this.addBookForm.enrollment
      }
      this.addBook(payload)
      this.initForm()
    },
    onSearch(evt) {
      evt.preventDefault()
      this.$refs.searchBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        course_id: this.searchForm.course_id,
        sec_id: this.searchForm.sec_id,
        year_semester: this.searchForm.year_semester,
        classroom_id: this.searchForm.classroom_id,
        time_slot_id: this.searchForm.time_slot_id,
        enrollment: this.searchForm.enrollment
      }
      this.searchBook(payload)
      this.initForm()
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
    },
    editBook(book) {
      this.editForm = book
    },
    onSubmitUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        course_id: this.editForm.course_id,
        sec_id: this.editForm.sec_id,
        year_semester: this.editForm.year_semester,
        classroom_id: this.editForm.classroom_id,
        time_slot_id: this.editForm.time_slot_id,
        enrollment: this.editForm.enrollment
      }
      this.updateBook(payload, this.editForm.course_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/sections/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Section updated!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onResetUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      this.initForm()
      this.getBooks() // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/sections/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Section removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.course_id)
    }
  }
}
</script>
